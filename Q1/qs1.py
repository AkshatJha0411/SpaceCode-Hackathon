import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "./exoplanets.csv"  # Replace with the actual path to your CSV file if different
data = pd.read_csv(file_path)

# Ensure the orbital period column is numeric
data['orbital_period'] = pd.to_numeric(data['orbital_period'], errors='coerce')

# Drop rows with missing or invalid orbital period values
data = data.dropna(subset=['orbital_period'])

# Focus on orbital periods between 0 and 400 days
data = data[(data['orbital_period'] >= 0) & (data['orbital_period'] <= 400)]

# Set custom colors
background_color = "#add8e6"  # Light blue
plot_color = "#1e3a5f"  # Dark blue

# Create the plot
plt.figure(figsize=(12, 7), facecolor=background_color)
plt.hist(
    data['orbital_period'], 
    bins=40, 
    edgecolor=plot_color, 
    color=plot_color, 
    alpha=0.9
)

# Customize the plot aesthetics
plt.title("Distribution of Exoplanets by Orbital Period", fontsize=18, fontweight='bold')
plt.xlabel("Orbital Period (days)", fontsize=14)
plt.ylabel("Number of Exoplanets", fontsize=14)

# Customize tick parameters
plt.xticks(fontsize=12, color=plot_color)
plt.yticks(fontsize=12, color=plot_color)

# Set the background color of the plot area
plt.gca().set_facecolor(background_color)

# Add tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()



