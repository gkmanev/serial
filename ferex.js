const serial = require('serialport');

// Configure serial port 2
const port2 = "/dev/FAKEFEREX"; // Replace with the appropriate serial port
const baudrate = 115200; // Replace with the appropriate baud rate

// Open serial port 2
const serialPort2 = new serial(port2, { baudRate: baudrate });

// Read from serial port 2 continuously
let buffer = Buffer.from('');
const startCharacter = Buffer.from([0x03]);
const bufferLength = 4;

serialPort2.on('data', data => {
    buffer = Buffer.concat([buffer, data]);

    // Process the buffer when the start character is found
    while (buffer.includes(startCharacter)) {
        const startIndex = buffer.indexOf(startCharacter);
        buffer = buffer.slice(startIndex);

        // Split the buffer into fixed-length binary buffers
        if (buffer.length >= bufferLength) {
            const binaryBuffer = buffer.slice(0, bufferLength);
            node.send({ payload: binaryBuffer.toString('hex') });
            buffer = buffer.slice(bufferLength);
        } else {
            // Break the loop if the buffer length is not sufficient
            break;
        }
    }
});