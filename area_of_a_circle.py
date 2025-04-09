def compute_area_of_circle(radius):
	pi = 3.14
	area = pi * radius * radius
	return area

def circ_area_str(radius, area):
	return f"The area of circle with radius {radius} is: {area}"

radius1 = 30
area1 = compute_area_of_circle(radius1)
print(circ_area_str(radius1, area1))

radius2 = 40
area2 = compute_area_of_circle(radius2)
print(circ_area_str(radius2, area2))
