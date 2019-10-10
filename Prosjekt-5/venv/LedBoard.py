import RPi.GPIO as GPIO
import time


# 13, 19, 26
class LedBoard:
    def __init__(self):
        # self.output_list = [4, 5, 6]
        self.pins = [13, 5, 26]

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
        print(self.pin_led_states[led_number])
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            print(pin_index,pin_state)
            self.set_pin(pin_index, pin_state)

 #       while True:
  #          x = int(input("Pin (0 to 5):"))
   #         self.light_led(x)

    def flash_all_leds(self, duration):
        """Flash all 6 LEDs on and off for k seconds"""
        for i in range(int(1000 * duration)):
            for i in range(0, 6):
                self.light_led(i)   # Set the leds to be output and HIGH
                time.sleep(0.1/600)

        for i in range(0, 3):
            self.set_pin(i, -1)  # Set the leds to be input and LOW

    def twinkle_all_leds(self, duration):
        """Turn all LEDs on and off in sequence for k seconds"""
        time_start = time.time()
        start_time = time_start - time.time()
        while start_time < duration:
            self.flash_all_leds(1)
            for i in range(0, 3):
                self.set_pin(i, -1)  # Sets the pins to LOW
            time.sleep(1)
            start_time = time.time()-time_start


    def power_up(self):
        """Pattern associated with powering up"""
        self.light_led(0)
        time.sleep(0.2)
        self.light_led(4)
        time.sleep(0.2)
        self.light_led(2)
        time.sleep(0.2)
        self.light_led(3)
        time.sleep(0.2)
        self.light_led(5)
        time.sleep(0.2)
        self.light_led(1)
        time.sleep(0.2)

        for i in range (0,2):
            self.set_pin(i,-1)

    def power_down(self):
        for i in range(3):
            self.flash_all_leds(0.5)

            self.set_pin(0, -1)
            self.set_pin(1, -1)
            self.set_pin(2, -1)
            time.sleep(0.5)

    def success(self):
        print("success")
        self.set_pin(0, 1)

    def failure(self):
        print("failure")
        self.set_pin(3, 1)
