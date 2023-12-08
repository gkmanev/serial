import paho.mqtt.client as mqtt
import serial
import time

# MQTT Broker Configuration
broker_address = "your_broker_address"
topic = "/pp/ubx/0236/Lb"  # Replace with your specific topic
client_id = "your_client_id"  # Replace with your MQTT client ID

# Serial Port Configuration for GNSS Receiver
serial_port = "COMx"  # Replace with your GNSS receiver's serial port
baud_rate = 9600  # Replace with your baud rate

# TLS Certificates (replace with your own file names)
cert_file = "path/to/certificate.crt"
key_file = "path/to/private/key.key"

# Callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(topic)
    else:
        print("Connection to MQTT Broker failed")

# Callback for when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print("Received message on topic:", msg.topic)
    print("Message:", msg.payload)
    
    # Forward received payload data to the GNSS receiver via serial
    gnss_serial.write(msg.payload)

# Initialize MQTT Client with TLS configuration
client = mqtt.Client(client_id=client_id)  # Set MQTT client ID here
client.on_connect = on_connect
client.on_message = on_message

# Set TLS configuration
client.tls_set(certfile=cert_file, keyfile=key_file)  # Add other parameters as needed

# Connect to MQTT Broker
client.connect(broker_address, port=8883)  # Use port 8883 for TLS connection

# Initialize Serial Connection for GNSS Receiver
gnss_serial = serial.Serial(port=serial_port, baudrate=baud_rate, timeout=0.1)

# Start MQTT Client Loop
client.loop_start()

try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    pass
finally:
    # Stop MQTT Client Loop and close serial connection
    client.loop_stop()
    gnss_serial.close()
