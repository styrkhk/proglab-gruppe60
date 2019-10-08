## import og include tidligere ark

class KPCAgent:

    def __init__(self):
        self.keypad = ##Keypad()
        self.led_board = ##LedBoard()
        self.password_file = ##Complete pathname to file holding the KPC's password
        self.password_buffer = ""
        self.new_password_buffer = ""
        self.override_signal = ""
        self.led_id = ""                        #Mulig dette må endres i forhold til led-board-koden
        self.led_dur = 0

    def init_passcode_entry(self):
        """Metode som initsialiserer password_buffer, kalles ved oppstart
        Kaller også power_up metoden på led_board"""
        self.password_buffer = ""
        # self.led_board.powerup() Må led_board må ha power_up-metode


    def get_next_signal(self):
        """hvis overridesignal, returner dette
        ellers, returner signalet fra keypad"""
        if self.override_signal:
            return self.override_signal
        else:
            return self.keypad.get_next_signal()        ##LEDBOARD MÅ HA METODEN get_next_signal


    def verify_login(self):
        """Sjekker input mot passord
        Kaller metoder i ledboard om suksess eller fiasko
        Setter Override-signal"""
        f = open(self.password_file, "r")
        password = f.read()
        f.close()

        if self.password_buffer == password:
            self.override_signal = "Y"
            self.led_board.success()    # Led-board må ha en success
        else:
            self.override_signal = "N"
            self.led_board.failure()    # Led-board må ha en failure metode


    def validate_passcode_change(self):
        """Validerer og endrer passord hvis validert"""
        if self.check_password_is_legal():
            f = open(self.password_file, "w")
            f.write(self.new_password_buffer)
            f.close()
            self.led_board.success()            # Led-board må ha en success
        else:
            self.led_board.failure()            # Led-board må ha en failure


    def check_password_is_legal(self):
        """Sjekker om nytt passord er lovlig"""
        if self.new_password_buffer.isnumeric() and len(self.new_password_buffer) >= 4:
            return True
        else:
            return False

    def light_one_led(self):
        """Litt usikker på hvordan denne bør utformes"""
        self.led_board.light_led(self.led_id, self.led_dur)     ##ledBoard må ha denne metoden

    def flash_leds(self):
        """kaller flash_leds på LED"""
        self.led_board.flash_all_leds()                         #ledBoard må ha denne metoden

    def twinkle_leds(self):
        """Kaller twinkle_leds på LED"""
        self.led_board.twinkle_all_leds()

    def exit_action(self):
        """Kaller power_down  på LED"""
        self.led_board.power_down()         #ledBoard må ha denne metoden


