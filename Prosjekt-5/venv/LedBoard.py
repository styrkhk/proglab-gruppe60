import RPi.GPIO as GPIO
import time


# 13, 19, 26
class LedBoard:
    def __init__(self):
        self.setup()
        # self.output_list = [4, 5, 6]

        self.pins = [13, 19, 26]

        self.pin_led_states = [
            [1, 0, -1],  # A
            [0, 1, -1],  # B
            [-1, 1, 0],  # C
            [-1, 0, 1],  # D
            [1, -1, 0],  # E
            [0, -1, 1]   # F
        ]

        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):

        if pin_state == -1:  # False
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def light_led(self, led_number): # OBS nr from 0 to 5
        """Turn on one of the 6 LEDs corresponding to button push"""
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            set_pin(pin_index, pin_state)

        set_pin(0, -1)
        set_pin(1, -1)
        set_pin(2, -1)

        while True:
            x = int(raw_input("Pin (0 to 5):"))
            light_led(x)

    def flash_all_leds(self, duration):
        """Flash all 6 LEDs on and off for k seconds"""
        for i in range[0, 5]:
            set_pin(i, 1)   # Set the leds to be output and HIGH
        time.sleep(duration)

        for i in range[0, 5]:
            set_pin(i, -1)  # Set the leds to be input and LOW

    def twinkle_all_leds(self, duration):
        """Turn all LEDs on and off in sequence for k seconds"""
        start_time = time.time()
        while start_time < duration:
            for i in range[0, 5]:
                set_pin(i, 1)  # Sets the pin to HIGH
            for i in range[0, 5]:
                set_pin(i, -1)  # Sets the pins to LOW


            for i in range[0, 5]:
                set_pin(i, -1)  # Sets the pins to LOW

    def power_up(self):
        """Pattern associated with powering up"""
        set_pin(0, 1)
        time.sleep(0.5)
        set_pin(1, 1)
        time.sleep(0.5)
        set_pin(2, 1)
        time.sleep(0.5)
        set_pin(3, 1)
        time.sleep(0.5)
        set_pin(4, 1)
        time.sleep(0.5)
        set_pin(5, 1)
        time.sleep(0.5)

        for i in range[0, 5]:
            set_pin(i, -1)  # Sets the pins to LOW

    def power_down(self):
        for i in range[0, 5]:
            set_pin(i, 1)  # Sets the pins to HIGH

        set_pin(0, -1)
        time.sleep(0.5)
        set_pin(1, -1)
        time.sleep(0.5)
        set_pin(2, -1)
        time.sleep(0.5)
        set_pin(3, -1)
        time.sleep(0.5)
        set_pin(4, -1)
        time.sleep(0.5)
        set_pin(5, -1)

    def success(self):
        print("success")
        set_pin(0, 1)

    def failure(self):
        print("failure")
        set_pin(3, 1)
