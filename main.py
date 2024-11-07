import random
import time
from azure.iot.device import IoTHubDeviceClient, Message


CONNECTION_STRING = "your_device_connection_string"

# Initialize the client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# Simulate temperature and humidity data
def simulate_sensor_data():
    while True:
        temperature = random.uniform(20.0, 35.0)  # Example temperature range in Celsius
        humidity = random.uniform(30.0, 80.0)    # Example humidity range in percentage

        # Create message JSON
        message = Message(f'{{"temperature": {temperature}, "humidity": {humidity}}}')
        client.send_message(message)
        print(f"Sent message: {message}")
        time.sleep(5)  # Adjust the frequency as needed

# Run the simulation
try:
    print("Sending sensor data to IoT Hub...")
    simulate_sensor_data()
except KeyboardInterrupt:
    print("Simulation stopped")
finally:
    client.shutdown()
