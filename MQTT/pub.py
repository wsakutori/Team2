# Base code for MQTT from tutorial: https://github.com/pholur/180D_sample
# Adjustments for reading existing .wav file and publishing

# POSSIBLE BROKERS
# mqtt.eclipse.org
# test.mosquitto.org
# broker.emqx.io

import time
import random
from paho.mqtt import client as mqtt_client
import sys
broker = 'mqtt.eclipseprojects.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'
sys.path.insert(1, '../../MQTT')

class PUB:
    def __init__(self, topic, msg):
        self.topic = topic
        self.msg = msg

    def set_msg(self, msg):
        self.msg = msg

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        # Set Connecting Client ID
        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client

    def publish_text(self, client):
         msg_count = 0
         for i in range(1, 2):
             time.sleep(1)
             result = client.publish(self.topic, self.msg)
             # result: [0, 1]
             status = result[0]
             if status == 0:
                 # print(f"Send `{msg}` to topic `{topic}`")
                 print(f"Sent message to topic `{self.topic}` and message `{self.msg}`")
             else:
                 print(f"Failed to send message to topic {self.topic}")
         # msg_count += 1

    def publish_file(self, client, file_path):
         msg_count = 0
         print(file_path)
         if file_path.rsplit('.',1)[1] == 'wav':
              for i in range(1, 10):
                  time.sleep(1)
                  #msg = f"messages: {msg_count}"
                  f = open(file_path, "rb")
                  filestr = f.read()
                  f.close()
                  msg = bytearray(filestr)
                  result = client.publish(self.topic, msg)
                  #result = client.publish(self.topic, self.msg)
                  # result: [0, 1]
                  status = result[0]
                  if status == 0:
                      # print(f"Send `{msg}` to topic `{topic}`")
                      print(f"Sent message to topic `{self.topic}`")
                  else:
                      print(f"Failed to send message to topic {self.topic}")
         else:
            for i in range(1, 3):
                time.sleep(1)
                #msg = f"messages: {msg_count}"
                f = open(file_path, "rb")
                filestr = f.read()
                f.close()
                msg = bytearray(filestr)
                result = client.publish(self.topic, msg)
                #result = client.publish(self.topic, self.msg)
                # result: [0, 1]
                status = result[0]
                if status == 0:
                    # print(f"Send `{msg}` to topic `{topic}`")
                    print(f"Sent message to topic `{self.topic}`")
                else:
                    print(f"Failed to send message to topic {self.topic}")

             # msg_count += 1


def run():
    pub=PUB("/team2/michelletan","hello")
    client = pub.connect_mqtt()
    client.loop_start()
    pub.publish_file(client, "test.wav")


if __name__ == '__main__':
    run()
