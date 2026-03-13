"""
Problem: Implement a heuristic algorithm for the Traveling Salesman Problem (TSP) using the nearest neighbor approach.
Result is in the README
"""
import math

def distance(a, b):
    # This function calculates the Euclidean distance between two points a and b
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx*dx + dy*dy)
    #return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def tsp_nearest_neighbor(cities):
    n = len(cities) # Number of cities
    visited = [False]*n
    path = [0]  # Start from the first city
    visited[0] = True
#iterate n-1 times to find the nearest unvisited city and add it to the path
    for _ in range(n-1):
        last = path[-1]
        next_city = min(
            [(i, distance(cities[last], cities[i])) for i in range(n) if not visited[i]],
            key=lambda x: x[1]
        )[0]
        path.append(next_city)
        visited[next_city] = True

    path.append(0)
    return path


cities = [(0,0), (2,3), (5,2), (6,6)]
tour = tsp_nearest_neighbor(cities)
print("Cities (coordinates):", cities)
print("Tour order (indices):", tour)
print("Tour coordinates:", [cities[i] for i in tour])
