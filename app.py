#!/usr/bin/python3

import os
import time, json
import paho.mqtt.publish as publish
from envirophat import light, motion, weather, leds
mqtt_broker = "10.0.3.11"

try:
    while True:
        lux = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ', '')
        leds.off()
        acc = str(motion.accelerometer())[1:-1].replace(' ', '')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
        values = {
            "temp": temp,
            "pressure": press, 
            "heading": heading,
            "accelerometer": acc,
            "light_level": lux,
            "light_colour": rgb
        }
        
        json_output = json.dumps(values)
        publish.single("home/garage/envirophat", json_output, hostname=mqtt_broker)
        time.sleep(5)

except KeyboardInterrupt:
    leds.off()
