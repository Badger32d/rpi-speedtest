# Python Speedtest app for Raspberry Pi

This is a simple app I wrote to run a speedtest and display it using this [very nice](https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi) display.

TODO: many things

* backlight change based on speed (green for within 80% of advertized, then yellow and red as speed degrades)
* storage of metrics in some form of DB, probably elasticsearch


I decided to check out the shiny new resin.io after I got the app working natively in raspbian.
While there are still some rough edges, I think they have a rather interesting project. Initial run takes forever,
partially due to the massive base container. I'll be experementing with making that container as small as possible.

## Parts

I'm using an OG raspberry pi, and the aforementioned [Adafruit RGB LCD+Keypad kit](https://www.adafruit.com/product/1109)

### Resin.io Setup & Deployment

1. If you haven't got a resin.io account, visit [resin.io](http://resin.io) and sign up.
1. start a new applicaton on resin.io, name it what you want, download the .zip file and extract it to your SD card.
1. Insert the SD card into the Raspberry pi, connect the ethernet cable and power it up.
1. After about 10 -15 minutes your device should show up on the resin.io applications dashboard.


Once your resin.io account is set up, you should be able to:

`$ git clone https://github.com/Badger32d/rpi-speedtest.git`

then add the resin remote: (replacing <myUserName> and <myApplicationName> with yours from the resin.io dashboard)

`$ git remote add resin git@git.staging.resin.io:<myUserName>/<myApplicationName>.git`

and finally push the code to your raspberry pi:

`$ git push resin master`
