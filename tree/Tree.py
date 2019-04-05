import sys


class Node:
    def __init__(self, v):
        self._value = v
        self._left = None
        self._right = None

    def __str__(self):
        return "{0._value}".format(self)

    @property
    def no_child(self):
        return True if self._left is None and self._right is None else False

    def insert(self, d):
        if self._value == d:
            return False
        elif self._value > d:
            if self._left:
                return self._left.insert(d)
            else:
                self._left = Node(d)
                return True
        else:
            if self._right:
                return self._right.insert(d)
            else:
                self._right = Node(d)
                return True

    def pre_order_print(self):
        sys.stdout.write(str(self) + ' ')
        if self._left is not None:
            self._left.pre_order_print()
        if self._right is not None:
            self._right.pre_order_print()

    def post_order_print(self):
        if self._left is not None:
            self._left.post_order_print()
        if self._right is not None:
            self._right.post_order_print()
        sys.stdout.write(str(self) + ' ')

    def delete(self, n):
        if self._left == n:
            if self._left.no_child:
                self._left = None
                return True
        elif self._right == n:
            if self._right.no_child:
                self._right = None
                return True
        else:
            if self._value > n:
                return self._left.delet(n)
            else:
                return self._right.delete(n)


class Tree:
    def __init__(self):
        self._root = None

    def insert(self, d):
        if self._root:
            return self._root.insert(d)
        else:
            self._root = Node(d)
            return True

    def pre_order_print(self):
        if self._root is not None:
            self._root.pre_order_print()

    def post_order_print(self):
        if self._root is not None:
            self._root.post_order_print()

    def delete_tree(self):
        self._root = None


if __name__ == '__main__':
    t = Tree()
    t.insert(4)
    t.insert(3)
    t.insert(5)
    t.insert(1)
    t.insert(2)
    t.pre_order_print()
    sys.stdout.write('\n')
    t.post_order_print()
