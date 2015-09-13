import RPi.GPIO as GPIO
from app.LEDController import LED
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

blue = LED(17, 'output')
green = LED(22, 'output')

def main():
    while True:
        GPIO.setwarnings(False)

        if GPIO.input(23):
            blue.flicker(0.5)
            green.flicker(0.5)
        else:
            blue.off()
            green.off()


def signal_handler(signal, frame):
    GPIO.cleanup()
    sys.exit()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
