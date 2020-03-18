from statistics import median


class Node:
    def __init__(self, value=0):
        try:
            self.__value = int(value)
        except (ValueError, TypeError):
            self.__value = 0
        finally:
            self.__parent = None
            self.__left = None  # left child
            self.__right = None  # right child

    def __repr__(self):
        if self is not None:
            return "Node"
        else:
            return "None"

    def __str__(self):
        return ("Value: " + str(self.__value) + "\n" + "Left child: " + repr(self.__left) + "\n" + "Right child: " +
                repr(self.__right) + "\n" + "Is a root? " + str(self.is_root()))

    def get_value(self):
        return self.__value

    def set_value(self, value):
        try:
            self.__value = int(value)
        except (ValueError, TypeError):
            self.__value = 0

    def get_parent(self):
        return self.__parent

    def __set_parent(self, parent):
        self.__parent = parent

    def is_root(self):
        if self.get_parent() is None:
            return True
        else:
            return False

    def get_left_child(self):
        return self.__left

    def get_right_child(self):
        return self.__right

    def add_child(self, child):
        if isinstance(child, Node) is False:
            return
        if self.__right is None:
            self.__right = child
        elif self.__left is None:
            self.__left = child
        else:
            if Tree.height(self.__left) < Tree.height(self.__right):
                self.__left.add_child(child)
            else:
                self.__right.add_child(child)
        child.__set_parent(self)


class Tree:
    @classmethod
    def height(cls, node):
        if isinstance(node, Node) is False:
            return 0
        left = cls.height(node.get_left_child())
        right = cls.height(node.get_right_child())
        return 1 + max(left, right)

    def print_tree(self, top):  # pre order method
        if isinstance(top, Node):
            print(top.get_value())
            self.print_tree(top.get_left_child())
            self.print_tree(top.get_right_child())

    def calc(self, top):
        values = []

        def pre_order(node):
            values.append(node.get_value())
            if node.get_left_child() is not None:
                pre_order(node.get_left_child())
            if node.get_right_child() is not None:
                pre_order(node.get_right_child())

        if isinstance(top, Node) is False:
            return None, None, None
        else:
            pre_order(top)
            val_sum = sum(values)
            average = val_sum / len(values)
            val_median = median(values)
            return val_sum, average, val_median


if __name__ == "__main__":
    root = Node(5)
    root.add_child(Node(7))
    root.add_child(Node(3))
    root.get_left_child().add_child(Node(5))
    root.get_left_child().add_child(Node(2))
    root.get_right_child().add_child(Node(0))
    root.get_right_child().add_child(Node(1))
    root.get_right_child().get_right_child().add_child(Node(8))
    root.get_right_child().get_right_child().add_child(Node(2))
    #  root.get_right_child().get_right_child().get_right_child().add_child(Node(5))
    root.get_right_child().get_right_child().add_child(Node(5))

    tree = Tree()
    tree.print_tree(root)
    results = tree.calc(root)
    print("Sum:", results[0])
    print("Average:", results[1])
    print("Median:", results[2])
