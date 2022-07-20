# iot-device-monitor-using-ML


# start zookerper
```
bin\windows\zookeeper-server-start.bat config\zookeeper.properties
```

# Start kafka
```
bin\windows\kafka-server-start.bat .\config\server.properties --override delete.topic.enable=true
```

# Create topic
```
bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic workshopkafka
```

# Consumer
```
bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic workshopkafka
```
