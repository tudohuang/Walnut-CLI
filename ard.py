import serial
import time
import serial.tools.list_ports

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "Arduino" in port.description:
            return port.device
    return None
user_input = input("hi:")
if user_input.startswith('!Arduino'):
                        arduino_port = find_arduino_port()
                        if arduino_port is None:
                            print("Arduino not found. Please check your connection.")
                        else:
                            # Initialize serial connection
                            ser = serial.Serial(arduino_port, 9600)

                            # Wait for the Arduino to initialize
                            time.sleep(3)

                            # Use the input provided to the function
                            _,user_inputa = user_input.split(' ')
                            #print(user_inputa)
                            # Send user input to Arduino
                            ser.write((user_inputa + '\n').encode())


