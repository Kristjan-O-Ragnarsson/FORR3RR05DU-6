"""
Kristjan O. Ragnarsson
Fyrir Reiknirit 2019/
For Algorithms 2019
Vertex Class
"""


class Vertex:
    """
    Vertex for _Graph
    """

    def __init__(self, _n):
        """
        Init
        :param _n: Name of Vertex
        """
        self._name = _n
        self.neighbors = set()

    @property
    def name(self):
        return self._name

    def add_neighbor(self, _v):
        """

        :param _v: Vertex to add as neighbor
        :return: None
        """
        if _v not in self.neighbors:
            self.neighbors.add(_v)


