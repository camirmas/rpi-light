import RPi.GPIO as GPIO
from app.LEDController import LED
import time
import signal
import sys

green = LED(17, 'output')
blue = LED(22, 'output')

def main():
    while True:
        GPIO.setwarnings(False)

        green.flicker(.5)
        blue.flicker(.5)

def signal_handler(signal, frame):
    GPIO.cleanup()
    sys.exit()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
