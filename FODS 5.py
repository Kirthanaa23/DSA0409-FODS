import numpy as np

# Fuel efficiency (in km/l) of 5 different vehicles
efficiency_data = np.array([14, 18, 21, 19, 16])

# Calculate the overall average fuel efficiency
avg_kmpl = np.mean(efficiency_data)

# Compare vehicle at index 1 and index 3
vehicle_a = efficiency_data[1]  # 18 km/l
vehicle_b = efficiency_data[3]  # 19 km/l

# Calculate efficiency gain from vehicle A to B
efficiency_gain = ((vehicle_b - vehicle_a) / vehicle_a) * 100

# Round and display
print(f"Overall average efficiency: {avg_kmpl:.2f} km/l")
print(f"Efficiency gain from Vehicle A to B: {efficiency_gain:.2f}%")

#OUTPUT
Overall average efficiency: 17.60 km/l  
Efficiency gain from Vehicle A to B: 5.56%

