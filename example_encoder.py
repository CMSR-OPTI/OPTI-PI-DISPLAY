import json
import random

# Generate random temperatures around room temperature (in Celsius)
temperatures = [random.uniform(20, 25) for _ in range(4)]

times = list(range(4))
times = [float(x) for x in times]

# Generate random GPS coordinates around CMU
cmu_coordinates = [
    {"latitude": random.uniform(40.434, 40.441), "longitude": random.uniform(-79.945, -79.933)}
    for _ in range(4)
]

# Generate random accelerations
accelerations = [
    {"x": random.uniform(-1, 1), "y": random.uniform(-1, 1), "z": random.uniform(-1, 1)}
    for _ in range(4)
]

# Create a dictionary containing all the data
data = {
    "times": times,
    "temperatures": temperatures,
    "cmu_coordinates": cmu_coordinates,
    "accelerations": accelerations
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data, indent=4)


# Specify the file path
file_path = "example_json_data.log"

# Open the file in write mode (if the file doesn't exist, it will be created)
with open(file_path, "w") as file:
    # Write the string to the file
    file.write(json_data)