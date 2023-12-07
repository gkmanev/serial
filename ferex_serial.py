import serial
import paho.mqtt.client as mqtt

# Configure serial port 2
port2 = "/dev/FAKEFEREX"  # Replace with the appropriate serial port
baudrate = 115200  # Replace with the appropriate baud rate

# Open serial port 2
serial_port2 = serial.Serial(port2, baudrate=baudrate, timeout=0)
mqtt_client = mqtt.Client()

# Read from serial port 2 continuously
buffer = b""
start_character = b'\x03'
buffer_length = 4

while True:
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
                
                buffer = buffer[buffer_length:]
            else:
                # Break the loop if the buffer length is not sufficient
                break
