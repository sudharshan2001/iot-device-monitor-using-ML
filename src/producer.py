
from kafka import KafkaProducer
import paho.mqtt.client as mqtt
from json import dumps

mqtt_topic = "workshop5MQTT"
kafka_topic = "workshopkafka"

def sendmessagetokafka(message):
    
    producer.send(kafka_topic, message)
    print("message is ", message)

def mqtt2kafka():
    client = mqtt.Client(client_id="mqtt2kafka")
    
    on_connect = lambda client, userdata,flags, rc: client.subscribe(mqtt_topic)
    client.on_connect = on_connect

    on_message = lambda client, userdata,message: sendmessagetokafka(message.payload.decode())
    client.on_message = on_message
    
    on_disconnect = lambda client, userdata,flags, rc:print("JOB Diconnected",client, userdata,flags)
    client.on_disconnect = on_disconnect

    client.connect("localhost", 1883, 60)
    client.loop_forever()

producer = KafkaProducer(bootstrap_servers="localhost:9092", value_serializer=lambda x: dumps(x).encode('utf-8'))
mqtt2kafka()


