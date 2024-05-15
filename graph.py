import pandas as pd
from vertex import Vertex
from edge import Edge

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def make_graph(self, file):
        df = pd.read_csv(file, dtype={'line': str})
        vertexes_names = set()
        for row in df.itertuples():
            edge = Edge(row.company, row.line, row.departure_time, row.arrival_time)
            dep_hour, dep_min, dep_sec = map(int, row.departure_time.split(':'))
            dep_time = dep_hour * 60 + dep_min
            arr_hour, arr_min, arr_sec = map(int, row.arrival_time.split(':'))
            arr_time = arr_hour * 60 + arr_min
            weight = arr_time - dep_time
            vertexes_names.add(row.start_stop)
            edge.weight = weight
            if row.start_stop not in self.vertices:
                self.vertices[row.start_stop] = Vertex(row.start_stop_lat, row.start_stop_lon)
            if row.end_stop not in self.vertices[row.start_stop].neighbours:
                self.vertices[row.start_stop].neighbours[row.end_stop] = []
            self.vertices[row.start_stop].neighbours[row.end_stop].append(edge)
        self.vertices['Żórawina - Niepodległości (Mostek)'] = Vertex(50.97974058, 17.04068965)
        return vertexes_names

    def draw_graph(self):
        plt.figure(figsize=(10, 6))

        # Rysowanie krawędzi
        for vertex_name, vertex in self.vertices.items():
            for neighbor_name, edge in vertex.neighbours.items():
                neighbor = self.vertices[neighbor_name]
                plt.plot([vertex.position1, neighbor.position1], [vertex.position2, neighbor.position2],
                         color='black')

        # Dodawanie wierzchołków (kropki i nazwy)
        for vertex_name, vertex in self.vertices.items():
            plt.plot(vertex.position1, vertex.position2, 'ro', markersize=10)
            plt.text(vertex.position1, vertex.position2, vertex_name, fontsize=12, ha='center', va='bottom')

        # Dodawanie osi
        plt.xlabel('Latitude')
        plt.ylabel('Longitude')
        plt.title('Graph Visualization')

        # Ustawienie równych skal na osiach x i y
        plt.axis('equal')

        # Wyświetlenie rysunku
        plt.show()

    def draw_vertices(self):
        plt.figure(figsize=(10, 6))

        # Rysowanie wierzchołków
        for vertex_name, vertex in self.vertices.items():
            plt.plot(vertex.position2, vertex.position1, 'ro', markersize=5)
            plt.text(vertex.position2, vertex.position1, vertex_name, fontsize=6, ha='center', va='bottom')
        for vertex in self.vertices.items():
            for des in vertex[1].neighbours.items():
                vertex2 = self.find_vertex(des[0])
                if vertex2 is not None:
                    start_pos = (vertex[1].position2, vertex[1].position1)
                    end_pos = (vertex2.position2, vertex2.position1)
                    plt.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color='black')

        plt.xlabel('Latitude')
        plt.ylabel('Longitude')
        plt.title('Vertices Visualization')

        plt.show()

    def find_vertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        else:
            print(name)
            return None



if __name__ == "__main__":
    grapgh = Graph()
    grapgh.make_graph('unique_edges.csv')
    grapgh.draw_vertices()

