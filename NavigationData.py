'''
@author: Devangini Patel
'''
import matplotlib.pyplot as plt

#connections between places
connections = {}
connections["Bus Stop"] = {"Library"}
connections["Library"] = {"Bus Stop", "Car Park", "Student Center"}
connections["Car Park"] = {"Library", "Maths Building", "Store"}
connections["Maths Building"] = {"Car Park", "Canteen"}
connections["Student Center"] = {"Library", "Store" , "Theater"}
connections["Store"] = {"Student Center", "Car Park", "Canteen", "Sports Center"}
connections["Canteen"] = {"Maths Building", "Store", "AI Lab"}
connections["AI Lab"] = {"Canteen"}
connections["Theater"] = {"Student Center", "Sports Center"}
connections["Sports Center"] = {"Theater", "Store"}

#location of all the places

location = {}
location["Bus Stop"] = [2, 8]
location["Library"] = [4, 8]
location["Car Park"] = [1, 4]
location["Maths Building"] = [4, 1]
location["Student Center"] = [6, 8]
location["Store"] = [6, 4]
location["Canteen"] = [6, 1]
location["AI Lab"] = [6, 0]
location["Theater"] = [7, 7]
location["Sports Center"] = [7, 5]

# Extract x and y coordinates
x_coords = [coord[0] for coord in location.values()]
y_coords = [coord[1] for coord in location.values()]

# Plot the locations
plt.scatter(x_coords, y_coords)

# Label the points
for location, (x, y) in location.items():
    plt.text(x, y, location)

# Add labels and title
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Locations')

# Show the plot
plt.show()