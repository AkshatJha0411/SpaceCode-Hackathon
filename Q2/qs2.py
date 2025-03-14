import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lombscargle

# Load the data from the file
file_path = "./RV_51Pegasi_Data.txt"  # Replace with your file path
data = np.genfromtxt(file_path, delimiter=None, encoding="utf-8-sig")

# Extract columns
time = data[:, 0]  # Column 1: Time in Julian date
radial_velocity = data[:, 1]  # Column 2: Radial velocity (m/s)
uncertainty = data[:, 2]  # Column 3: Uncertainty in Radial Velocity (m/s)

# Task 1: Scatter Plot of Radial Velocity Data
plt.figure(figsize=(10, 6))
plt.scatter(
    time, radial_velocity, color='blue', s=80, label='Radial Velocity Data'
)  # 's' controls the size of the markers
plt.xlabel("Time (Julian Date)", fontsize=12)
plt.ylabel("Radial Velocity (m/s)", fontsize=12)
plt.title("Radial Velocity of 51 Pegasi", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Task 3: Lomb-Scargle Periodogram Analysis
# Define frequencies for the periodogram
frequencies = np.linspace(0.1, 1.0, 10000)  # Range: 0.1 to 1.0 cycles/day

# Normalize time and radial velocity
time_normalized = time - np.min(time)  # Shift time to start from zero
rv_mean = np.mean(radial_velocity)
radial_velocity_normalized = radial_velocity - rv_mean

# Perform Lomb-Scargle periodogram
angular_frequencies = 2 * np.pi * frequencies  # Convert frequencies to angular frequencies
power = lombscargle(time_normalized, radial_velocity_normalized, angular_frequencies)

# Identify the best frequency
best_frequency = frequencies[np.argmax(power)]
orbital_period = 1 / best_frequency  # Convert frequency to period

# Plot the periodogram
plt.figure(figsize=(10, 6))
plt.plot(1 / frequencies, power, color='blue')  # Period (1/frequency) on x-axis
plt.axvline(orbital_period, color='red', linestyle='--', label=f'Best Period: {orbital_period:.2f} days')
plt.xlabel("Period (days)", fontsize=12)
plt.ylabel("Power", fontsize=12)
plt.title("Lomb-Scargle Periodogram", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"The estimated orbital period from the Lomb-Scargle periodogram is {orbital_period:.2f} days.")

# Task 4: Folded Radial Velocity Curve
# Use the orbital period derived from the periodogram
# Replace `orbital_period` with the derived value if needed
phase = (time % orbital_period) / orbital_period

# Sort the data by phase for better visualization
sorted_indices = np.argsort(phase)
phase_sorted = phase[sorted_indices]
radial_velocity_sorted = radial_velocity[sorted_indices]
uncertainty_sorted = uncertainty[sorted_indices]

# Plot the folded radial velocity curve
plt.figure(figsize=(10, 6))
plt.errorbar(
    phase_sorted, radial_velocity_sorted, yerr=uncertainty_sorted,
    fmt='o', color='blue', ecolor='gray', elinewidth=1, capsize=3, markersize=6,
    label='Folded Radial Velocity Data'
)
plt.xlabel("Phase", fontsize=12)
plt.ylabel("Radial Velocity (m/s)", fontsize=12)
plt.title("Folded Radial Velocity Curve of 51 Pegasi", fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
