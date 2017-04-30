#!/usr/bin/env python

import subprocess
import time

import Adafruit_CharLCD as LCD

class SpeedTestCheck(object):

    def __init__(self):
        self.current = {}

    def setup(self):
        self.lcd = LCD.Adafruit_CharLCDPlate()
        self.lcd.set_color(0.0, 0.0, 1.0)

    def checkspeed(self):
        self.lcd.clear()
        self.lcd.set_color(1.0, 0.0, 1.0)
        self.lcd.message("Checking speed....")
        cmd = "speedtest-cli --simple --secure"
        raw = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, errors = raw.communicate()
        cleaned = filter(None, output.split('\n'))
        self.current = dict(map(str, x.split(':')) for x in cleaned)
        print self.current

    def printspeed(self):
        if self.current['Download'].split('.')[0] > 35:
            self.lcd.clear()
            self.lcd.set_color(0.0, 1.0, 0.0)
        elif self.current['Download'].split('.')[0] < 35:
            self.lcd.clear()
            self.lcd.set_color(1.0, 0.0, 0.0)
        msg1 = "Down: {0} Mb/s".format(self.current['Download'].split('.')[0]) + '\n' + "Up: {0} Mb/s".format(self.current['Upload'].split('.')[0])
        self.lcd.message(msg1)

    def main(self):
        self.setup()
        while True:
            try:
                self.checkspeed()
            except Exception as e:
                print "could not check speed: %s" %(e)
            try:
                self.printspeed()
            except Exception as e:
                print "could not display speed: %s" %(e)
            time.sleep(3600)



if __name__ == '__main__':
    stc = SpeedTestCheck()
    stc.main()
