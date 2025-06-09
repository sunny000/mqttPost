#micropython script for pico w
from machine import Pin, I2C
import time 
import network
from umqtt.simple import MQTTClient

import WiFi # local wifi connection module
from getTime import formatted_time



mqtt_server = 'broker.emqx.io'
client_id = 'bigles4567'
topic_pub = b'test'
topic_msg = b'testing from pico w @ ' + formatted_time


def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(.5)
    machine.reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()

client.publish(topic_pub, topic_msg)
    
