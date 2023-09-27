"""

do not forget to deactivate from the venv when you running this from the IDE terminal.
Before running start the servers with these commands in the CLI.
1.  C:/kafka/kafka_2.13-3.5.1/bin/windows/zookeeper-server-start.bat C:/kafka/kafka_2.13-3.5.1/config/zookeeper.properties

2. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-server-start.bat C:/kafka/kafka_2.13-3.5.1/config/server.properties

3. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-console-producer.bat --topic gps_app --bootstrap-server localhost:9092

4. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-console-consumer.bat --topic gps_app --bootstrap-server localhost:9092

create a new topic-- only first time use
C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-topics.bat --create --topic gps_app --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
"""

from flask import Flask, request, jsonify
from kafka import KafkaProducer
import threading
from kafka import KafkaConsumer
from json import *
import datetime
import os
import json
app = Flask(__name__)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

@app.route('/owntracks', methods=['POST'])
def owntracks_data():
    data = request.get_json()  # Parse the JSON data sent by OwnTracks
    if len(data)>1:##process_raw data
         # send it producer right away in kafka
         print("Sending to producer")
         producer.send("gps_app", value=data)
         producer.flush()
         return jsonify({"msg": "processed", "status": 200})
    else:
        return("Bad data")

def consume():
        try :
            consumer = KafkaConsumer("gps_app", bootstrap_servers=['localhost:9092'],
                                 value_deserializer=lambda x: loads(x.decode('utf-8')),
                                 auto_offset_reset="latest")
            for i in consumer:
                #print(i)
                #return(i.value)
                yield i.value
                #consumer.flush()
        except Exception as e:
            print("Consumer Error",e)

file_lock=threading.Lock()
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
def write_to_text_file(x):
    print("Writing to file")
    file_name = f"log_{current_date}.txt"
    with file_lock:
        if not os.path.exists(file_name):
            open(file_name,"w").close()

        data_str = json.dumps(x)
        with open(file_name,"a") as file:
            file.write(data_str+"/n")


if __name__ == '__main__':
    # Create a separate thread for the Kafka consumer
    consumer_thread = threading.Thread(target=consume)
    consumer_thread.daemon = True  # Daemonize the thread to allow it to exit when the main program exits
    consumer_thread.start()
    # Create a separate thread for writing data to a text file
    file_writer_thread = threading.Thread(target=write_to_text_file)
    file_writer_thread.daemon = True
    file_writer_thread.start()
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app on a desired host and port






