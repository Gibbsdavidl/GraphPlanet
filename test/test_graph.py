

import unittest
from src import graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        print("Running test-graph")
        self.g = graph.Graph("test1","non")

    def test_edgeListWithWeights(self):
        self.g.edgeListWithWeights("data/bollobas100.txt")
        self.assertTrue(self.g.numVertices() > 0)

    def test_addEdge(self):
        self.g.edgeListWithWeights("data/bollobas100.txt")
        self.assertTrue(self.g.numVertices() > 0)
        nold = self.g.numVertices()
        eold = self.g.numEdges()
        self.g.addEdgeWithWt("asdf","qwer",0.2)
        nnew = self.g.numVertices()
        enew = self.g.numEdges()
        self.assertTrue(nold + 2 == nnew)
        self.assertTrue(eold + 1 == enew)

    def test_remEdge(self):
        self.g.edgeListWithWeights("data/bollobas100.txt")
        self.assertTrue(self.g.numVertices() > 0)
        nold = self.g.numVertices()
        eold = self.g.numEdges()
        self.g.remEdge("82","40")
        nnew = self.g.numVertices()
        enew = self.g.numEdges()
        self.assertTrue((nold-1) == nnew)
        self.assertTrue((eold-1) == enew)



if __name__ == '__main__':
    unittest.main()
