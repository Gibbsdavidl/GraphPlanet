from unittest import TestCase
from src import graph
from src import search

__author__ = 'David L Gibbs'


class TestSearch(TestCase):

    def setUp(self):
        print("Running test-search")
        self.g1 = graph.Graph("dfstest1", "non")
        self.g1.edgeList("data/searchgraph.txt")
        self.g2 = graph.Graph("dfstest2", "directed")
        self.g2.edgeList("data/searchgraph.txt")

    def test_dfs(self):
        soln = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        res0 = search.dfs(self.g1,"a")
        print(res0)
        self.assertTrue(res0 == soln)


    def test_bfs(self):
        def wanted(v):
            if v == 'j':
                return(True)
            else:
                return(False)
        soln = 'j'
        self.assertTrue(search.bfs(self.g1,"a",wanted) == soln)


    def test_lexBfs(self):
        soln = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'f']
        result = search.lexBfs(self.g1)
        self.assertTrue(result == soln)

    def test_toposort(self):
        soln = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'f']
        result = search.toposort(self.g1)
        print (result)
        self.assertTrue(result == soln)



if __name__ == '__main__':
    unittest.main()
