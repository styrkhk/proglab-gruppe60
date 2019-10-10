from typing import List, Union, Callable



class Rule:
    def __init__(self, current_state: Union[str, List[str]], next_state: str, signal: Union[str, Callable[[str], bool]], action: str):
        self.cur_state = current_state
        self.next_state = next_state
        self.signal = signal
        self.action = action

    def get_current_state(self):
        return self.cur_state

    def get_next_state(self):
        return self.next_state

    def get_trigger_signal(self):
        return self.signal

    def get_action(self):
        return self.action


def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57


def is_signal(signal):
    return signal is not None


def signal_is_valid_led_id(signal):
    return 48 <= ord(signal) <= 53


def signal_is_N_or_hashtag(signal):
    return signal == "N" or signal == "#"


def signal_is_N_or_star(signal):
    return signal == "N" or signal == "*"


def signal_is_star_or_hashtag(signal):
    return signal == "*" or signal == "#"

def signal_is_Y_or_star(signal):
    return signal == "Y" or signal == "*"
