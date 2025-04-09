import math

def calculate_volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

def sphr_area_str(radius, volume):
	return f"The volume of sphere with radius {radius} is: {volume}"

radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(sphr_area_str(radius1, volume1))

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print(sphr_area_str(radius2, volume2))
