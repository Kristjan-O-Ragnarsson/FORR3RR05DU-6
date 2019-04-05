from sys import stdout
from _Graph import *
from collections import defaultdict


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

    def print_graph_dfs(self, _v, visited):
        """
        dfs printing
        :param _v: Vertex
        :param visited: Visited dict
        :return: recursiv stuff
        """
        visited[_v] = True
        stdout.write(str(_v) + '\n')
        for i in sorted(list(self.vertices[_v].neighbors)):
            if visited.get(i) == False:
                self.print_graph_dfs(i, visited)

    def DFS(self, _v):
        """
        DEF Print
        :param _v: Vertex
        :return: None
        """

        _visited = defaultdict()
        for i in self.vertices.keys():
            _visited[i] = False
        # print _visited
        self.print_graph_dfs(_v, _visited)

    def print_graph_bfs(self, _v, _visited):
        """
        Breadth first search
        :param _v: Vertex
        :param _visited: Visited list
        :return: Recursive stuff
        """
        pass

    def BFS(self, _v):
        """
        Breadth first search Print function
        :param _v: Vertex
        :return:  None
        """
        _visited = defaultdict()
        for i in sorted(list(self.vertices.keys())):
            _visited[i] = False
        # print _visited
        self.print_graph_bfs(_v, _visited)

        queue = []

        queue.append(_v)

        _visited[_v] = True

        while queue:
            _n = queue.pop(0)
            stdout.write(str(_n) + '\n')

            for i in  sorted(list(self.vertices.keys())):
                if _visited[i] == False:
                    queue.append(i)
                    _visited[i] = True

if __name__ == '__main__':
    g = Graph()
    a = Vertex('A')
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))
    g.add_vertex(Vertex('C'))
    g.add_vertex(Vertex('D'))
    g.add_vertex(Vertex('E'))
    g.add_vertex(Vertex('F'))
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')
    g.add_edge('D', 'F')
    g.add_edge('E', 'F')
    #g.print_graph()
    print "from A"
    g.BFS('A')
