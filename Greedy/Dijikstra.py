"""
Problem: Find the shortest distance from a starting node to all other nodes in a graph using Dijkstra's algorithm.
Result is in the README
"""
import heapq #using queue

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} # set distances to all nodes as infinity
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        # gets node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)
# visits each neighbor
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'D': 1},
    'C': {'B': 2, 'D': 5},
    'D': {}
}
print("DIJKSTRA'S ALGORITHM:")
print(dijkstra(graph, 'A'))