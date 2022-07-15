from email import message
import pandas as pd
import sys
import json
from paho.mqtt import client as mqtt
import time

df = pd.read_csv("home2.csv", error_bad_lines=False,low_memory=False)

i=0
host_ = "localhost"
port = 1883
options = 60
topic_name = "IOT_DEVICE"

while True:
    if i<len(df):
        temp = df.iloc[i]
        json_temp = temp.to_dict()
        
        message = json.dumps(json_temp)
        
        client=mqtt.Client()
        client.connect(host_, port, options)
        
        client.publish(topic_name, message)
        client.disconnect()
        time.sleep(1)
        i+=1

    else:
        print("Done")
        sys.exit(1)