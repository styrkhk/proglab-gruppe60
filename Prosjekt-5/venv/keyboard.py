import RPi.GPIO as GPIO
import time
class Keypad:



    def __init__(self):
        self.setup()
        self.key = None
        self.coordinates_to_numbers = {(0,0):1,(0,1):4, (0,2):7,(0,3):"*", (1,0):2,(1,1):5,(1,2):8,(1,3):0,(2,0):3,(2,1):6,(2,2):9,(2,3):"#"}
        self.row = {0:18,1:23,2:12,3:16}
        self.column = {0:17,1:27,2:22}
        self.number = None
        self.key_pressed = False

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        GPIO.setup(12,GPIO.OUT)
        GPIO.setup(16,GPIO.OUT)
        GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


    def do_polling(self):

        for r in range (0,4):
            GPIO.output(self.row[r],GPIO.HIGH)

            for c in range (0,3):
                counter = 0
                a = True
                while GPIO.input(self.column[c]) == GPIO.HIGH and a :
                    counter +=1
                    time.sleep(0.01)
                    if counter == 20:
                        self.key = (c,r)
                        self.number = self.coordinates_to_numbers[self.key]
                        self.key_pressed = True
                        a = False
                        print(self.number)
                        time.sleep(1)
            GPIO.output(self.row[r],GPIO.LOW)

    def get_next_signal(self):
        self.key_pressed = False
        while self.key_pressed == False:
            self.do_polling()
        return self.number
        print("number returnert")



