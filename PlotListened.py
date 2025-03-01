import matplotlib.pyplot as plt
import csv

# Define the CSV filename
csv_filename = "sensor_data.csv"

# Lists to store the data for plotting
time_stamps = []
current_amps = []
battery_voltage = []
accel_x = []
accel_y = []
accel_z = []

# Read the CSV file and extract the data
with open(csv_filename, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    
    for row in reader:
        time_stamps.append(len(time_stamps))  # Time based on data points (or replace with actual timestamps)
        current_amps.append(float(row[0]))
        battery_voltage.append(float(row[1]))
        accel_x.append(float(row[2]))
        accel_y.append(float(row[3]))
        accel_z.append(float(row[4]))

# Plotting the data
plt.figure(figsize=(10, 8))

# Plot current (amps)
plt.subplot(2, 2, 1)
plt.plot(time_stamps, current_amps, label="Current (A)", color='blue')
plt.xlabel('Time')
plt.ylabel('Current (A)')
plt.title('Current Over Time')
plt.grid(True)

# Plot battery voltage (V)
plt.subplot(2, 2, 2)
plt.plot(time_stamps, battery_voltage, label="Battery Voltage (V)", color='green')
plt.xlabel('Time')
plt.ylabel('Voltage (V)')
plt.title('Battery Voltage Over Time')
plt.grid(True)

# Plot accelerometer data
plt.subplot(2, 2, 3)
plt.plot(time_stamps, accel_x, label="Accel X (m/s²)", color='red', linestyle='--')
plt.plot(time_stamps, accel_y, label="Accel Y (m/s²)", color='orange', linestyle='--')
plt.plot(time_stamps, accel_z, label="Accel Z (m/s²)", color='purple', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Acceleration (m/s²)')
plt.title('Accelerometer Data Over Time')
plt.legend()
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.show()
