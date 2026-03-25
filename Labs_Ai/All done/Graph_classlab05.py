
# !=========Question 1=========
# from collections import deque
# class Graph:
#     def __init__(self):
#         self.edge={}
#     def add_vertex(self,vertex):
#         self.edge[vertex]=deque()
#     def add_edge(self,vertex1,vertex2):
#         self.edge[vertex1].append(vertex2)
#         self.edge[vertex2].append(vertex1)
#     def print(self):
#         for vertex,neighbors in self.edge.items():
#             print(f"{vertex}: {list(neighbors)}")
# g=Graph()
# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_edge("A","B")
# g.add_edge("B","C")
# g.print()
# !=========Question 2=========
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
class Graph:
    def __init__(self):
        self.edges = {}

    def add_vertex(self, vertex):
        if vertex not in self.edges:
            self.edges[vertex] = deque()


    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.edges[vertex2]:
            self.edges[vertex1].append(vertex2)
        if vertex2 not in self.edges[vertex1]:
            self.edges[vertex2].append(vertex1)
    

    def print_edges(self):
        for vertex, neighbors in self.edges.items():
            print(f"{vertex}:{list(neighbors)}")


graph2 = Graph()
graph2.add_vertex("A")
graph2.add_vertex("B")
graph2.add_vertex("C")
graph2.add_edge("A", "B")
graph2.add_edge("B", "C")
graph2.add_edge("A", "C")
graph2.print_edges()

graph2 = Graph()
vertices = ["Seattle","San Francisco", "Los Angeles", "Denver", "khanas City", "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston"]
edges = [[0,1], [0,3], [0,5],[1,2],[1,3],[2,3],[2,4],[2,10],[3,4],[3,5],[4,5],[4,6],[5,6],[5,7],[6,7],[7,8],[8,9],[8,10],[8,11],[9,11],[10,11]]
for vertex in vertices:
    graph2.add_vertex(vertex)
for edge in edges:
    graph2.add_edge(vertices[edge[0]], vertices[edge[1]])


graph2.print_edges()
g = nx.Graph()
g.add_nodes_from(vertices)
nx_edges = [(vertices[edge[0]], vertices[edge[1]]) for edge in edges]
g.add_edges_from(nx_edges)

nx.draw(g, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
plt.title("Graph Visualization")
plt.show()