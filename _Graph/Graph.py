from sys import stdout
from _Graph import *


class Graph:
    """
    _Graph Class
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, _u, _v):
        if _u in self.vertices and _v in self.vertices:
            for key, value in self.vertices.items():
                if key == _u:
                    value.add_neighbor(_v)
                if key == _v:
                    value.add_neighbor(_u)
            return True
        else:
            return False

    def print_graph(self):
        """
        NOT ANY SPESIFIC TRAVERSAL as far as i know
        :return:
        """
        for key in sorted(list(self.vertices.keys())):
            stdout.write(str(key) + ' ' + str(self.vertices[key].neighbors) + '\n')


if __name__ == '__main__':
    g = Graph()
    a = Vertex('A')
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))
    g.add_vertex(Vertex('C'))
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.print_graph()
