import math

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def tsp_nearest_neighbor(cities):
    n = len(cities)
    visited = [False]*n
    path = [0]  
    visited[0] = True

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
print(tour)
