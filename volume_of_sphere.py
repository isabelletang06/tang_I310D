import math

def calculate_volume_of_sphere(radius):
    return (4/3) * math.pi * radius**3

# Compute and print the volume for radii 30 and 40
print("Volume of sphere with radius 30:", calculate_volume_of_sphere(30))
print("Volume of sphere with radius 40:", calculate_volume_of_sphere(40))
