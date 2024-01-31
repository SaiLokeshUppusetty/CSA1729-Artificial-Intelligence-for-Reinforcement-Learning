import numpy as np

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor(cities, start_city):
    unvisited_cities = set(cities)
    current_city = start_city
    tour = [current_city]

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: calculate_distance(current_city, city))
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(start_city)  # Return to the starting city to complete the tour
    return tour

def total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Example usage:
if __name__ == "__main__":
    # Example cities represented as (x, y) coordinates
    cities = [(0, 0), (1, 2), (2, 4), (3, 1), (5, 3)]

    # Start the tour from the first city
    start_city = cities[0]

    # Find the tour using the Nearest Neighbor algorithm
    tour = nearest_neighbor(cities, start_city)

    # Print the tour and total distance
    print("Tour:", tour)
    print("Total Distance:", total_distance(tour))
