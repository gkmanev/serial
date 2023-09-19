import serial
import paho.mqtt.client as mqtt
# Configure serial port 1
port1 = "/dev/ttyACM0"  # Replace with the appropriate serial port
baudrate = 115200  # Replace with the appropriate baud rate
# Configure MQTT broker
mqtt_broker = "172.17.0.1"  # Replace with the IP address or hostname of your MQTT broker
mqtt_port = 1883  # Replace with the MQTT broker port
mqtt_topic = "gps"  # Replace with the desired MQTT topic

mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)


# Open serial port 1
serial_port1 = serial.Serial(port1, baudrate=baudrate, timeout=0)

# Read from serial port 1 continuously
buffer = ""
start_character = "$"

while True:
    data = serial_port1.read(100)
    if data:
        print(data)
        buffer += data.decode()

        # # Process the buffer when the start character is found
        # while start_character in buffer:
        #     start_index = buffer.index(start_character)
        #     buffer = buffer[start_index:]

        #     # Split the buffer at newline character
        #     newline_index = buffer.find("\n")
        #     if newline_index != -1:
        #         ascii_string = buffer[:newline_index].strip()
        #         print(ascii_string)
        #         mqtt_client.publish(mqtt_topic, ascii_string)
        #         buffer = buffer[newline_index + 1:]
        #     else:
        #         # Break the loop if newline character is not found yet
        #         break
