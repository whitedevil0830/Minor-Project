import networkx as nx

# Create a graph representing the road network
G = nx.Graph()

# Add nodes representing locations
G.add_node('place1')
G.add_node('place2')
G.add_node('place3')

# Add edges representing roads and their lengths
G.add_edge('place1', 'place2', weight=10)
G.add_edge('place2', 'place3', weight=15)
G.add_edge('place1', 'place3', weight=20)

# Calculate heuristic values based on shortest paths to a goal location
goal_location = 'place3'
heuristic_values = {}

for node in G.nodes:
    shortest_path_length = nx.shortest_path_length(G, node, goal_location, weight='weight')
    heuristic_values[node] = shortest_path_length

print("Heuristic values based on road length:")
print(heuristic_values)

from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of the Earth in kilometers

    return distance

# Example coordinates for two places
lat1, lon1 = 20.295433, 85.824245   # Latitude and longitude for Berlin, Germany
lat2, lon2 = 20.279104, 85.798981   # Latitude and longitude for Paris, France

# Calculate distance between the two places using Haversine formula
distance = haversine(lat1, lon1, lat2, lon2)
print("Distance between the two places:", distance, "km")
