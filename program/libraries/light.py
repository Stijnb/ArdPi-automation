import time
from error import CustomException

class Light():

    def __init__(self):

        self.inputDb = {}
        self.timers = {}
        self.calcTimeUnit = {'s': 0, 'm': 60, 'h': 3600}

    def onOff(self, id, entry, output):
        """
        Set a output on or off.
        Use this function with a pushbutton.

        :param id: Give this function a id
        :param entry: Give the status of the input
        :param output: Give the status if the ouput
        """
        if self.inputDb.has_key(id) is False:

            self.inputDb = {id: False}

        if self.inputDb[id] == entry:

            return output

            self.inputDb[id] = entry

        else:

            if entry and output:

                self.inputDb[id] = entry

                return False

            elif entry and output is False:

                self.inputDb[id] = entry

                return True

    def dimming(self, entry, marker, output_value):
        """

        :param entry:
        :param marker:
        :param output_value:
        :return:
        """
        if entry and marker:

            output_value - 10

        elif entry and marker is False:

            output_value + 10

        elif entry is False and marker:

            marker_value = False

        elif entry is False and marker is False:

            marker_value = True

        return {'marker': marker_value, 'output': output_value}

    def startTimer(self, name, timeValue):
        """
        Here you can make a timer.
        These function is used bij on and off delay timer.

        :param name: The name of the timer
        :param timeValue: time value in seconds
        :return:
        """
        begin = int(time.time())
        end = begin + timeValue

        self.timers[name] = {'begin': time.time(), 'time': timeValue, 'end': end}

    def checkTimer(self, name):
        """
        Check of the timer is expired and delete the timer.

        :param name: The name of the timer
        :return: True timer is passed
        """

        if time.time() >= self.timers[name]['end']:

            del self.timers[name]

            return True

        else:

            return False

    def offDelay(self, entry, name, timeValue, timeUnit):
        """
        Set a off delay timer.
        The output is constantly true, when the timer is passed the output come False

        :param entry: The value of the input
        :param name: The name of the input
        :param timeValue: The time value(100, 1, 34, ...)
        :param timeUnit: s -> seconds, m -> minutes, h - hours
        :return:
        """
        calc = int(timeValue * self.calcTimeUnit[timeUnit])

        if entry == True:

            self.startTimer(name, calc)

            return True

        else:

            if self.checkTimer(name):

                return True

            else:

                return False






