import unittest

import bayesian
from bayesian._domain import Node

class TestDomainGraph(unittest.TestCase):
    """Test the DomainGraph class"""
    
    def test_simplicial_node(self):
        """Test the simplicial_node property"""

        node1 = Node('A')
        node2 = Node('B')
        node3 = Node('C')
        node4 = Node('D')
        node5 = Node('E')

        graph = bayesian.DomainGraph()
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)
        graph.add_node(node4)
        graph.add_node(node5)

        # Add the links. There are no links between nodes 1 and 3.
        node1.add_link(node2)
        node2.add_link(node3)
        node3.add_link(node4)
        node4.add_link(node1)
        node5.add_link(node1)
        node5.add_link(node2)
        node5.add_link(node3)
        node5.add_link(node4)

        # There are no simplicial nodes in the graph.
        self.assertTrue(graph.simplicial_node is None)

        # Add a link to make it triangulated.
        node4.add_link(node2)
        self.assertTrue(graph.simplicial_node is not None)

if __name__ == '__main__':
    unittest.main()
