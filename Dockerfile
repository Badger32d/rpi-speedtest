FROM resin/raspberrypi-debian

ENV INITSYSTEM on

RUN echo i2c-bcm2708 >> /etc/modules
RUN echo i2c-dev >> /etc/modules

RUN apt-get update && \
apt-get install -y python python-pip python-smbus i2c-tools python-dev build-essential && \
pip install speedtest-cli Adafruit-CharLCD && \
pip install -U RPi.Gpio && rm -rf /var/lib/apt/lists/*

COPY . /app

CMD ["python", "/app/SpeedTestCheck.py"]
