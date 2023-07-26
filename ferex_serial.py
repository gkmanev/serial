import serial
import paho.mqtt.client as mqtt
import time

# Configure serial port 2
port2 = "/dev/ttyUSB0"  # Replace with the appropriate serial port
baudrate = 115200  # Replace with the appropriate baud rate

# Configure MQTT broker
mqtt_broker = "172.17.0.1"  # Replace with the MQTT broker address
mqtt_port = 1883  # Replace with the MQTT broker port
mqtt_topic = "ferex"  # MQTT topic to publish the binary buffers

# Open serial port 2
serial_port2 = serial.Serial(port2, baudrate=baudrate, timeout=0)
mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)

# Read from serial port 2 continuously
buffer = b""
start_character = b'\x03'
buffer_length = 4

def connect_to_serial():
    while True:
        try:
            serial_port2.open()
            print("Serial device connected!")
            break
        except serial.SerialException as e:
            print(f"Serial device not available: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

connect_to_serial()

while True:
    try:
        data = serial_port2.read(100)
        if data:
            buffer += data

            # Process the buffer when the start character is found
            while start_character in buffer:
                start_index = buffer.index(start_character)
                buffer = buffer[start_index:]

                # Split the buffer into fixed-length binary buffers
                if len(buffer) >= buffer_length:
                    binary_buffer = buffer[:buffer_length]
                    print(binary_buffer)
                    mqtt_client.publish(mqtt_topic, binary_buffer)
                    buffer = buffer[buffer_length:]
                else:
                    # Break the loop if the buffer length is not sufficient
                    break
    
    except serial.SerialException as e:
        print(f"Serial device disconnected: {e}")
        print("Reconnecting...")
        connect_to_serial()
