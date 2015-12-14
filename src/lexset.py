
__author__ = "David L Gibbs"
__project__ = "GraphPlanet"


# a set that's kept sorted in lexical order.
# used in the lexBFS

import bisect

class LexSet:

    def lexadd(self,b):
        if b not in self.lexset:
            bisect.insort(self.lexset,b)

    def lexpop(self):
        head = self.lexset[0]
        self.lexset = self.lexset[1:]
        return head

    def tolist(self):
        return self.lexset

    def toset(self):
        return set(self.lexset)

    def intersection(self, ns):
        return([])

    def setdiff(self, ns):
        return([])

    def __init__(self,a):
        self.length = len(a)
        self.lexset = list(a)
        self.lexset.sort()
