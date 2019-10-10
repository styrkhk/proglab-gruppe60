## import og include tidligere ark
import Ledboard as led
import Keyboard as key


class KPCAgent:

    def __init__(self):
        self.keypad = key.Keypad()
        self.led_board = led.LedBoard()
        self.password_file = "pw.txt"  ##Complete pathname to file holding the KPC's password
        self.password_buffer = ""
        self.new_password_buffer = ""
        self.override_signal = ""
        self.led_id = 0
        self.led_dur = 0

    def init_passcode_entry(self):
        """Metode som initsialiserer password_buffer, kalles ved oppstart
        Kaller også power_up metoden på led_board"""
        self.password_buffer = ""
        self.led_board.power_up()
        print("Initialised password inputs")

    def reset_agent(self):
        self.password_buffer = ""
        self.new_password_buffer = ""
        self.led_board.flash_all_leds()
        print("Agent reset")

    def get_next_signal(self):
        """hvis overridesignal, returner dette
        ellers, returner signalet fra keypad"""
        if len(self.override_signal):
            tmp = self.override_signal
            self.override_signal = ""
        else:
            tmp = ""
            while len(tmp) == 0:
                tmp = self.keypad.get_next_signal()
        print("Got signal from keypad: ", tmp)
        return tmp

    def verify_login(self):
        """Sjekker input mot passord
        Kaller metoder i ledboard om suksess eller fiasko
        Setter Override-signal"""
        f = open(self.password_file, "r")
        password = f.read()
        f.close()

        if self.password_buffer == password:
            self.override_signal = "Y"
            self.led_board.success()
            print("Logged in! ")
        else:
            self.override_signal = "N"
            self.led_board.failure()
            print("Login failure")

    def validate_passcode_change(self):
        """Validerer nytt passord"""
        if self.check_password_is_legal():
            self.led_board.success()
            self.override_signal = "Y"
            print("New password validated")
        else:
            self.led_board.failure()
            self.override_signal = "N"
            print("New password failed")

    def check_password_is_legal(self):
        """Sjekker om nytt passord er lovlig"""
        if self.password_buffer.isnumeric() and len(self.password_buffer) >= 4:
            return True
        else:
            return False

    def change_password(self):
        f = open(self.password_file, "w")
        f.write(self.password_buffer)
        f.close()
        self.led_board.success()
        print("Password changed")

    #    def create_new_password(self, letter):
    #        self.new_password_buffer = self.new_password_buffer+letter
    #        print("New Password Buffer: ", self.new_password_buffer)

    #    def append_next_password_digit(self, letter: str):
    #        self.new_password_buffer += letter
    #        print("Added to new password: ", letter, "New password: ", self.new_password_buffer)

    def create_buffered_password(self, letter: str):
        self.password_buffer = self.password_buffer + letter
        print("Password Buffer: ", self.password_buffer)

    def set_led_id(self, letter: str):
        self.led_id = int(letter)
        print("Led, ", self.led_id, "set")

    def light_one_led(self):
        self.led_board.light_led(self.led_id, self.led_dur)
        print("Light in led: ", self.led_id, "for ", self.led_dur, "seconds")

    def reset_duration(self):
        self.led_dur = 0
        print("Led duration reset")

    def set_duration(self, letter: str):
        self.led_dur = int(letter)
        print("Led duration set: ", self.led_dur)

    def flash_leds(self):
        """kaller flash_leds på LED"""
        self.led_board.flash_all_leds(self.led_dur)

    def twinkle_leds(self):
        """Kaller twinkle_leds på LED"""
        self.led_board.twinkle_all_leds(self.led_dur)

    def exit_action(self):
        """Kaller power_down  på LED"""
        self.led_board.power_down()
        print("Program exit")

    def do_action(self, action: str, symbol: str):
        if action == "a0":
            print("Nothing")
        elif action == "a1":
            self.init_passcode_entry()
        elif action == "a2":
            self.create_buffered_password(symbol)
        elif action == "a3":
            self.verify_login()
        elif action == "a4":
            self.reset_agent()
        elif action == "a5":
            self.twinkle_leds()
        elif action == "a6":
            self.set_led_id(symbol)
        elif action == "a7":
            self.reset_duration()
        elif action == "a8:":
            self.set_duration(symbol)
        elif action == "a9":
            self.light_one_led()
        elif action == "a10":
            self.validate_passcode_change()
        elif action == "a11":
            self.change_password()
        elif action == "a12":
            self.exit_action()

