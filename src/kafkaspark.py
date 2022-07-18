from pyspark.sql.session import SparkSession  
from pyspark.sql.functions import *
# import findspark
# findspark.add_packages('mysql:mysql-connector-java:8.0.11')

spark = SparkSession.builder.appName("kafkaStreaming").master("local[*]")\
    .config("spark.mongodb.input.uri", "mongodb://localhost/workshopkafkaiot.kafka_mqtt") \
        .config("spark.mongodb.output.uri", "mongodb://localhost/workshopkafkaiot.kafka_mqtt") \
            .getOrCreate()


spark.sparkContext.setLogLevel("Error")

# df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "workshopkafka").load()
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "workshopkafka") \
  .load()

df1 = df.selectExpr("cast(value as string) as kafka_output").withColumn("kafka_output_new", 
        regexp_replace("kafka_output","\\\\","")).drop("kafka_output")

df1.writeStream.format("console").option('truncate','false').outputMode("Append").start()

def mongoInsert(dataframe,epoch_id):
    dataframe.write.format("mongo").mode("append").save()

df1.writeStream.foreachBatch(mongoInsert).start().awaitTermination()

# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0,org.mongodb.spark:mongo-spark-connector_2.12:2.4.1,org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.2 kafkaspark.py
