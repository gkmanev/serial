import serial

port1 = "/dev/ttyACM0"  # Replace with your serial port
baudrate = 115200  # Replace with the appropriate baud rate

try:
    serial_port1 = serial.Serial(port1, baudrate=baudrate, timeout=0)
    while True:
        data = serial_port1.read(100)
        if data:
            print(data)
except Exception as e:
    print(f"Error: {e}")
finally:
    serial_port1.close()
