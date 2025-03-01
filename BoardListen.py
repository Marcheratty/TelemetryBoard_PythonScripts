import serial
import csv

# Replace with the correct serial port and baud rate for your setup
SERIAL_PORT = 'COM5'  # Replace with the actual COM port for your device
# SERIAL_PORT = '/dev/ttyUSB0'  # For Linux/Unix
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Define the CSV file
csv_filename = "sensor_data.csv"

# Open CSV file in append mode to add data over time
with open(csv_filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Writing header only if the file is empty
    if file.tell() == 0:
        writer.writerow([
            "Current (A)", "Battery Voltage (V)", "Accel X (m_s2)", "Accel Y (m_s2)", "Accel Z (m_s2)",
            "Gyro H (deg)", "Gyro R (deg)", "Gyro P (deg)", "Latitude", "Longitude", "GPS Status"
        ])
    
    while True:
        try:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            if line.startswith("S"):
                # Parse the comma-separated values from the line
                data = line.split(',')
                
                # Ensure the line has the correct number of data points
                if len(data) == 12:
                    current_amps = float(data[1])
                    battery_voltage = float(data[2])
                    accel_x = float(data[3])
                    accel_y = float(data[4])
                    accel_z = float(data[5])
                    gyro_h = float(data[6])
                    gyro_r = float(data[7])
                    gyro_p = float(data[8])
                    latitude = float(data[9])
                    longitude = float(data[10])
                    gps_status = data[11]
                    
                    # Write the parsed data to the CSV file
                    writer.writerow([
                        current_amps, battery_voltage, accel_x, accel_y, accel_z,
                        gyro_h, gyro_r, gyro_p, latitude, longitude, gps_status
                    ])
                    print(f"Data saved: {data}")
        except Exception as e:
            print(f"Error reading or processing data: {e}")
            continue
import serial
import csv
import os

# Replace with the correct serial port and baud rate for your setup
SERIAL_PORT = 'COM3'  # Replace with the actual COM port for your device
BAUD_RATE = 9600

# Define the CSV file
csv_filename = "sensor_data.csv"

# Open CSV file in write mode to erase the old data every time the program starts
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Writing the header to the file
    writer.writerow([
        "Current (A)", "Battery Voltage (V)", "Accel X (m_s2)", "Accel Y (m_s2)", "Accel Z (m_s2)",
        "Gyro H (deg)", "Gyro R (deg)", "Gyro P (deg)", "Latitude", "Longitude", "GPS Status"
    ])
    
    # Open serial port
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

    while True:
        try:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            if line.startswith("S"):
                # Parse the comma-separated values from the line
                data = line.split(',')
                
                # Ensure the line has the correct number of data points
                if len(data) == 12:
                    current_amps = float(data[1])
                    battery_voltage = float(data[2])
                    accel_x = float(data[3])
                    accel_y = float(data[4])
                    accel_z = float(data[5])
                    gyro_h = float(data[6])
                    gyro_r = float(data[7])
                    gyro_p = float(data[8])
                    latitude = float(data[9])
                    longitude = float(data[10])
                    gps_status = data[11]
                    
                    # Write the parsed data to the CSV file
                    writer.writerow([
                        current_amps, battery_voltage, accel_x, accel_y, accel_z,
                        gyro_h, gyro_r, gyro_p, latitude, longitude, gps_status
                    ])
                    print(f"Data saved: {data}")
        except Exception as e:
            print(f"Error reading or processing data: {e}")
            continue
