#!/usr/bin/env python

import subprocess
import time

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate


class SpeedTestCheck(object):

    def __init__(self):
        self.current = {}

    def setup(self):
        self.lcd = Adafruit_CharLCDPlate()
        self.lcd.backlight(self.lcd.GREEN)

    def checkspeed(self):
        cmd = "speedtest-cli --simple --secure"
        raw = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, errors = raw.communicate()
        cleaned = filter(None, output.split('\n'))
        self.current = dict(map(str, x.split(':')) for x in cleaned)
        print self.current

    def printspeed(self):
        self.lcd.clear()
        self.lcd.backlight(self.lcd.BLUE)
        msg1 = "D" + self.current['Download'] + '\n' + "U" + self.current['Upload']
        self.lcd.message(msg1)

    def main(self):
        self.setup()
        while True:
            try:
                self.checkspeed()
            except Exception as e:
                print "not sure what happened! %s" %(e)
            try:
                self.printspeed()
            except Exception as e:
                print "not sure what happened! %s" %(e)
            time.sleep(3600)



if __name__ == '__main__':
    stc = SpeedTestCheck()
    stc.main()