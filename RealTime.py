import serial
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Replace with the correct serial port and baud rate for your setup
SERIAL_PORT = 'COM5'  # Replace with the actual COM port for your device
BAUD_RATE = 9600

# Define the CSV filename
csv_filename = "sensor_data.csv"

# Lists to store the data for plotting
time_stamps = []
latitude = []
longitude = []
gyro_h = []  # Heading
gyro_r = []  # Roll
gyro_p = []  # Pitch
accel_x = []
accel_y = []
accel_z = []

# Open serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Function to update the plot in real-time
def update_plot(frame):
    try:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        
        if line.startswith("S"):  # Checking for valid start character 'S'
            # Parse the comma-separated values from the line
            data = line.split(',')
            
            # Ensure the line has the correct number of data points
            if len(data) == 12:
                current_amps = float(data[1])
                battery_voltage = float(data[2])
                accel_x_val = float(data[3])
                accel_y_val = float(data[4])
                accel_z_val = float(data[5])
                gyro_h_val = float(data[6])
                gyro_r_val = float(data[7])
                gyro_p_val = float(data[8])
                latitude_val = float(data[9])
                longitude_val = float(data[10])
                gps_status = data[11]

                # Append the data to respective lists
                time_stamps.append(len(time_stamps))  # Use time based on the number of data points
                latitude.append(latitude_val)
                longitude.append(longitude_val)
                gyro_h.append(gyro_h_val)
                gyro_r.append(gyro_r_val)
                gyro_p.append(gyro_p_val)
                accel_x.append(accel_x_val)
                accel_y.append(accel_y_val)
                accel_z.append(accel_z_val)

                # Update the CSV file with the new data
                with open(csv_filename, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        current_amps, battery_voltage, accel_x_val, accel_y_val, accel_z_val,
                        gyro_h_val, gyro_r_val, gyro_p_val, latitude_val, longitude_val, gps_status
                    ])
                
                # Update the plots with new data
                ax1.clear()
                ax2.clear()
                ax3.clear()

                # Plot Position (Latitude vs Longitude)
                ax1.plot(longitude, latitude, label="Position (Lon vs Lat)", color='blue')
                ax1.set_xlabel('Longitude')
                ax1.set_ylabel('Latitude')
                ax1.set_title('Position (Latitude vs Longitude)')
                ax1.grid(True)

                # Plot Orientation (Gyroscope Euler Angles: Heading, Roll, Pitch)
                ax2.plot(time_stamps, gyro_h, label="Gyro Heading (deg)", color='red')
                ax2.plot(time_stamps, gyro_r, label="Gyro Roll (deg)", color='green')
                ax2.plot(time_stamps, gyro_p, label="Gyro Pitch (deg)", color='purple')
                ax2.set_xlabel('Time')
                ax2.set_ylabel('Angle (deg)')
                ax2.set_title('Gyroscope Orientation Over Time')
                ax2.legend()
                ax2.grid(True)

                # Plot Acceleration (Accelerometer X, Y, Z)
                ax3.plot(time_stamps, accel_x, label="Accel X (m/s²)", color='orange')
                ax3.plot(time_stamps, accel_y, label="Accel Y (m/s²)", color='cyan')
                ax3.plot(time_stamps, accel_z, label="Accel Z (m/s²)", color='magenta')
                ax3.set_xlabel('Time')
                ax3.set_ylabel('Acceleration (m/s²)')
                ax3.set_title('Accelerometer Data Over Time')
                ax3.legend()
                ax3.grid(True)

                # Refresh the figure
                plt.draw()
    except Exception as e:
        print(f"Error reading or processing data: {e}")
        pass

# Create figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

# Use FuncAnimation to update the plot in real-time
ani = animation.FuncAnimation(fig, update_plot, interval=1000)  # Update every 1 second

# Show the plot
plt.tight_layout()
plt.show()
