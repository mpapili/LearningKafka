from kafka import KafkaConsumer, TopicPartition

# set up our consumer
consumer = KafkaConsumer(
        ### 'test',
        bootstrap_servers='localhost:9092',
        group_id='my-group', # Specify the consumer group
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        auto_commit_interval_ms=1_000, # commit every second)
)

# set it up to replay from the beginning
# Assign a specific topic and partition
topic_partition = TopicPartition('test', 0)  # Assuming partition 0
consumer.assign([topic_partition])

# Set the desired offset (e.g., 100 offsets back)
desired_offset = 100
consumer.seek(topic_partition, desired_offset)


for message in consumer:
    print(f"Received: {message.value}")

