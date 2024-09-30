import random as rn
import numpy as np
from math import radians, sin, cos, sqrt, asin
from numpy.random import choice as np_choice

class AntColony(object):

    def __init__(self, cities, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        Args:
        cities (list): List of tuples containing city name and coordinates (latitude, longitude).
        n_ants (int): Number of ants running per iteration.
        n_best (int): Number of best ants who deposit pheromone.
        n_iteration (int): Number of iterations.
        decay (float): Rate at which pheromone decays.
        alpha (int or float): Exponent on pheromone, higher alpha gives pheromone more weight. Default=1.
        beta (int or float): Exponent on distance, higher beta gives distance more weight. Default=1.
        """
        self.cities = cities
        self.distances = self._compute_distances()
        self.pheromone = np.ones(self.distances.shape) / len(self.cities)
        self.all_inds = range(len(self.cities))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def _compute_distances(self):
        """
        Calculates the distance matrix between all cities based on their coordinates.
        """
        distances = np.zeros((len(self.cities), len(self.cities)))
        for i in range(len(self.cities)):
            for j in range(i + 1, len(self.cities)):
                # Calculate distance using Haversine formula (or any other distance metric)
                lat1, lon1 = self.cities[i][1]
                lat2, lon2 = self.cities[j][1]
                
                lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
                R = 6371 # Radius of earth in kilometers. Use 3956 for miles. 

                # haversine formula 
                dlat = lat2 - lat1 
                dlon = lon2 - lon1 
                a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
                c = 2 * asin(sqrt(a)) 
                distance = c * R

                distances[i, j] = distance  # calculated distance
                distances[j, i] = distances[i, j]  # ensure symmetrical matrix
        return distances

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheromone(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            print(shortest_path)
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            self.pheromone = self.pheromone * self.decay
        return all_time_shortest_path

    def spread_pheromone(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1.0 / (self.distances[move] + 1e-6)

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            # if len(visited) == len(self.cities):  # if all cities have been visited
            #     visited = set() 
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        # Avoid division by zero and small values in denominator
        dist = np.clip(dist, 1e-6, np.inf)  # clip values between epsilon and infinity
        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)

        # Add a small base value to pheromone before normalization (optional)
        row += 1e-6 

        norm_row = row / row.sum()
        unvisited_options = np.where(norm_row > 0)[0]
        move = np_choice(unvisited_options, 1, p=norm_row[unvisited_options])[0]
        return move


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

    # Hyperparameters (adjust these as needed)
    n_ants = 50
    n_best = 20
    n_iterations = 100
    decay = 0.98 #rho
    alpha = 1
    beta = 1

    # Create the AntColony object
    ac = AntColony(cities, n_ants, n_best, n_iterations, decay, alpha, beta)
    shortest_path, distance = ac.run()

    # Extract city names from the shortest path
    route = [cities[i][0] for i, _ in shortest_path]

    # Print the shortest path and distance
    print("Shortest path:", shortest_path)
    # print("Route:", route)
    print("Total distance:", distance)

    

