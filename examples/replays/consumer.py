from kafka import KafkaConsumer

consumer = KafkaConsumer(
        'test',
        bootstrap_servers='localhost:9092',
        group_id='my-group', # Specify the consumer group
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        auto_commit_interval_ms=1_000, # commit every second)
)
for message in consumer:
    print(f"Received: {message.value}")

