import RPi.GPIO as GPIO
import time

class System():

    def __init__(self):
        """
        Setup the GPIO output's and input's of the raspberry PI.

        :return:
        """

        # GPIO setup of the RPI
        GPIO.setmode(GPIO.BOARD)

        self.ledRun = 11
        self.ledFault = 12
        self.ledCommunication = 13

        GPIO.setup(self.ledRun, GPIO.OUT)
        GPIO.setup(self.ledFault, GPIO.OUT)
        GPIO.setup(self.ledCommunication, GPIO.OUT)

        # Other var...
        self.timer = {}

    def run(self):
        """
        Set the run led on.

        :return:
        """
        GPIO.output(self.ledRun, 1)
        GPIO.output(self.ledFault, 0)

    def fault(self):
        """
        Set the fault led on and the run led off.

        :return:
        """
        GPIO.output(self.ledRun, 0)

        if self.timer.has_key('fault'):

            if self.checkTimer('fault', 1):

                self.setTimer('fault')

                if GPIO.input(self.ledFault):

                    GPIO.output(self.ledFault, 0)

                else:

                    GPIO.output(self.ledFault, 1)

        else:

            self.setTimer('fault')

    def setTimer(self, name):
        """
        Save the start time.
        :param name: the name of the timer
        :return:
        """

        self.timer[name] = int(time.time())

    def checkTimer(self, name, seconds):
        """
        Check if the time of the timer is expired.
        :param name: The name of the timer.
        :param seconds: The time that the timer must run.
        :return: True if expired.
        """
        if (self.timer[name] + seconds) > int(time.time()):
            return False

        else:
            return True

    def cleanUp(self):
        """
        Cleanup the GPIO of the raspberry Pi

        :return:
        """
        GPIO.cleanup()
