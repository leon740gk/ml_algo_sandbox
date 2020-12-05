# Python program to print all paths from a source to destination.
# https://www.geeksforgeeks.org/find-paths-given-source-destination/
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_all_paths_util(self, u, d, visited, path, mapper):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path) if not mapper else print([mapper[p] for p in path])
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.print_all_paths_util(i, d, visited, path, mapper)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    def print_all_paths(self, s, d, mapper=None):

        # Mark all the vertices as not visited
        visited = [False] * (self.vertices)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.print_all_paths_util(s, d, visited, path, mapper)


if __name__ == "__main__":
    g = Graph(8)
    cities_map = {
        "Moscow": 0,
        "London": 1,
        "Paris": 2,
        "Amsterdam": 3,
        "Berlin": 4,
        "New York": 5,
        "Las Vegas": 6,
        "Toronto": 7,
    }
    reverse_cities_map = {v: k for k, v in cities_map.items()}

    g.add_edge(cities_map["Moscow"], cities_map["London"])
    g.add_edge(cities_map["Moscow"], cities_map["Paris"])
    g.add_edge(cities_map["Paris"], cities_map["Amsterdam"])
    g.add_edge(cities_map["Paris"], cities_map["Berlin"])
    g.add_edge(cities_map["Berlin"], cities_map["Las Vegas"])
    g.add_edge(cities_map["Amsterdam"], cities_map["New York"])
    g.add_edge(cities_map["New York"], cities_map["Toronto"])
    g.add_edge(cities_map["London"], cities_map["Toronto"])
    g.add_edge(cities_map["Berlin"], cities_map["Toronto"])

    source = cities_map["Moscow"]
    destination = cities_map["Toronto"]
    print(f"Following are all different paths from "
          f"{reverse_cities_map[source]} to "
          f"{reverse_cities_map[destination]} :\n")

    g.print_all_paths(source, destination, reverse_cities_map)
