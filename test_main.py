import unittest
import main


class TestNode(unittest.TestCase):
    def test_set_value(self, value1=-2, value2=3.8435, value3=None, value4="four"):
        node1 = main.Node()
        # value1
        node1.set_value(value1)
        self.assertEqual(node1.get_value(), value1)
        # value2
        node1.set_value(value2)
        self.assertEqual(node1.get_value(), 3)
        # value3
        node1.set_value(value3)
        self.assertEqual(node1.get_value(), 0)
        # value4
        node1.set_value(value4)
        self.assertEqual(node1.get_value(), 0)

    def test_is_root(self):
        node1 = main.Node()
        node2 = main.Node()
        node1.add_child(node2)
        # node1
        self.assertTrue(node1.is_root())
        # node2
        self.assertFalse(node2.is_root())

    def test_get_left_child(self):
        node1 = main.Node()
        self.assertEqual(node1.get_left_child(), None)  # without left child
        node2 = main.Node()
        node1.add_child(node2)
        self.assertEqual(node1.get_left_child(), None)  # without left child
        node3 = main.Node()
        node1.add_child(node3)
        self.assertEqual(node1.get_left_child(), node3)  # with left child

    def test_get_right_child(self):
        node1 = main.Node()
        self.assertEqual(node1.get_right_child(), None)  # without right child
        node2 = main.Node()
        node1.add_child(node2)
        self.assertEqual(node1.get_right_child(), node2)  # with right child

    def test_add_child(self):
        node1 = main.Node()
        node1.add_child(2)
        node1.add_child("Node(2)")
        self.assertEqual(node1.get_left_child(), None)
        self.assertEqual(node1.get_right_child(), None)
        node2 = main.Node(2)
        node1.add_child(node2)
        self.assertEqual(node1.get_right_child(), node2)
        self.assertEqual(node1.get_left_child(), None)
        node3 = main.Node(3)
        node4 = main.Node(4)
        node1.add_child(node3)
        node1.add_child(node4)
        self.assertEqual(node1.get_left_child(), node3)
        self.assertEqual(node1.get_right_child().get_right_child(), node4)


class TestTree(unittest.TestCase):
    def test_height(self):
        self.assertEqual(main.Tree.height(3), 0)
        self.assertEqual(main.Tree.height("five"), 0)
        self.assertEqual(main.Tree.height(None), 0)
        node1 = main.Node(1)
        node2 = main.Node(1)
        node3 = main.Node(1)
        node4 = main.Node(1)
        self.assertEqual(main.Tree.height(node1), 1)
        node1.add_child(node2)
        self.assertEqual(main.Tree.height(node1), 2)
        node1.add_child(node3)
        self.assertEqual(main.Tree.height(node1), 2)
        node1.add_child(node4)
        self.assertEqual(main.Tree.height(node1), 3)
        self.assertEqual(main.Tree.height(node2), 2)
        self.assertEqual(main.Tree.height(node3), 1)
        self.assertEqual(main.Tree.height(node4), 1)

    def test_calc(self):
        tree = main.Tree()
        self.assertEqual(tree.calc(2), (None, None, None))
        self.assertEqual(tree.calc("Ten"), (None, None, None))
        self.assertEqual(tree.calc(None), (None, None, None))
        root = main.Node(5)
        self.assertEqual(tree.calc(root), (5, 5, 5))
        root.add_child(main.Node(7))
        self.assertEqual(tree.calc(root), (12, 6, 6))
        root.add_child(main.Node(3))
        self.assertEqual(tree.calc(root), (15, 5, 5))
        root.get_left_child().add_child(main.Node(5))
        self.assertEqual(tree.calc(root), (20, 5, 5))
        node = main.Node(-10)
        root.get_left_child().add_child(node)
        self.assertEqual(tree.calc(root), (10, 2, 5))
        self.assertEqual(tree.calc(node), (-10, -10, -10))


if __name__ == "__main__":
    unittest.main()
