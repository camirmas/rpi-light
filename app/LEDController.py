import RPi.GPIO as GPIO
import time
from threading import Timer

class LED():
    def __init__(self, channel, input_output):
        """
        Control an LED given a GPIO channel
        """
        self.channel = channel

        if input_output == 'input':
            self.input_output = GPIO.IN
        elif input_output == 'output':
            self.input_output = GPIO.OUT
        else:
            raise ValueError('Invalid parameter, please choose "input" or "output"')


    def setUp(self):
        """set up input/output channel"""

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, self.input_output)

    def on(self):
        """turn on an LED"""
        self.setUp()
        GPIO.output(self.channel, GPIO.HIGH)

    def off(self):
        """turn off an LED"""
        self.setUp()
        GPIO.output(self.channel, GPIO.LOW)

    def flicker(self, interval):
        """turn on/off on an interval"""
        self.on()
        time.sleep(interval)
        self.off()
