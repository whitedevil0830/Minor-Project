# from math import radians, sin, cos, sqrt, asin
# import numpy as np, 
import math
class NearestNeighbor:
    """
    A class implementing the Nearest Neighbor algorithm for TSP.
    """

    def __init__(self, city_data):
        """
        Initializes the algorithm with city data.

        Args:
            city_data: A list of city data, where each element is a tuple containing
                city name (string) and its coordinates (latitude, longitude) as a tuple.
        """
        self.city_data = city_data
        self.start_city = city_data[0]

    def haversine_distance(self, coord1, coord2):
        """Calculates the Euclidean distance between two coordinates."""
        lat1, lon1 = coord1
        lat2, lon2 = coord2

        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        R = 6371 # Radius of earth in kilometers. Use 3956 for miles. 

        # haversine formula 
        dlat = lat2 - lat1 
        dlon = lon2 - lon1 
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        return c * R

    def solve(self):
        """
        Implements the Nearest Neighbor algorithm and returns the visiting order.

        Returns:
            A list representing the visiting order of cities (city names).
        """
        visited = []
        total_distance = 0
        remaining = set(self.city_data)
        current_city = self.start_city  # Choose any starting city
        visited.append(current_city[0])  # Append city name
        remaining.remove(current_city)

        while remaining:
            nearest_city = None
            min_distance = float("inf")
            for city, coords in remaining:
                distance = self.haversine_distance(coords, current_city[1])
                if distance < min_distance:
                    nearest_city = (city, coords)
                    min_distance = distance
            visited.append(nearest_city[0])
            total_distance += min_distance
            current_city = (nearest_city, coords)
            remaining.remove(nearest_city)

        return_distance = self.haversine_distance(current_city[1], self.start_city[1])
        total_distance += return_distance
        return visited, total_distance


if __name__ == "__main__":
    cities = [
        ("bhubaneswar", (20.27241, 85.83385)),
        ("delhi", (28.65195, 77.23149)),
        ("kolkata", (22.56263, 88.36304)),
        ("Jaipur", (26.91962, 75.7873)),
        ("Srinagar", (34.08333, 74.83333)),
        ("ranchi", (23.34316, 85.3094)),
        ("Gandhinagar", (23.21667, 72.68333)),
        ("Thiruvananthapuram", (8.4855, 76.94924)),
        ("Shillong", (25.56892, 91.88313)),
        ("Shimla", (28.69275, 74.57112)),
        ("Agartala", (23.83605, 91.27939)),
    ]

    nn = NearestNeighbor(cities)
    route, total_distance = nn.solve()
    print("Route:", route)
    print("Total Route Length:", total_distance)