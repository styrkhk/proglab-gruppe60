from KPC import *
from Rules import *
from inspect import *



class FSM:
    def __init__(self):
        self.KPC = KPCAgent()

        self.cur_state = "s-init"
        self.cur_action = "a0"
        self.cur_symbol = 0
        self.rules = []

        self.add_rules("s-init", "s-read", is_signal, "a1")

        self.add_rules("s-read", "s-read", signal_is_digit, "a2")
        self.add_rules("s-read", "s-verify", "*", "a3")
        self.add_rules(["s-read", "s-verify"], "s-init", signal_is_N_or_hashtag, "a4")

        self.add_rules("s-verify", "s-active", "Y", "a5")

        self.add_rules("s-active", "s-led", signal_is_valid_led_id, "a6")
        self.add_rules("s-active", "s-logout", "#", "a0")
        self.add_rules(["s-active", "s-validate"], "s-change", signal_is_N_or_star, "a4")

        self.add_rules("s-change", "s-change", signal_is_digit, "a2")
        self.add_rules("s-change", "s-validate", "*", "a10")
        self.add_rules("s_change", "s-active", "#", "a0")

        self.add_rules("s-validate", "s-init", "Y", "a11")

        self.add_rules("s-led", "s-duration", "*'", "a7")

        self.add_rules("s-duration", "s-duration", signal_is_digit, "a8")
        self.add_rules("s-duration", "s-active", "*", "a9")

        self.add_rules("s-logout", "s-active", "*", "a0")
        self.add_rules("s-logout", "s-end", "#", "a12")

    def add_rules(self, current_state: Union[str, List[str]], next_state: str,
                  signal: Union[str, Callable[[str], bool]], action: str):
        self.rules.append(Rule(current_state, next_state, signal, action))

    def fire_rule(self, rule: Rule):
        self.cur_state = rule.next_state
        self.cur_action = rule.action
        self.KPC.do_action(self.cur_action, self.cur_symbol)

    def apply_rule(self, rule: Rule):
        cor_state = False
        if isinstance(rule.cur_state, List):
            for state in rule.cur_state:
                if self.cur_state == state:
                    cor_state = True
        elif isinstance(rule.cur_state, str):
            if self.cur_state == rule.cur_state:
                cor_state = True
        cor_symbol = False
        if isfunction(rule.signal):
            cor_symbol = rule.signal(self.cur_symbol)
        elif isinstance(rule.signal, str):
            cor_symbol = rule.signal == self.cur_symbol
        return cor_state and cor_symbol

    def run_rules(self):
        for rule in self.rules:
            if self.apply_rule(rule):
                self.fire_rule(rule)
                break

    def main_loop(self):
        self.cur_state = "s-init"
        while self.cur_state != "s-end":
            self.cur_symbol = self.KPC.get_next_signal()
            self.run_rules()




FSM = FSM()
FSM.main_loop()
