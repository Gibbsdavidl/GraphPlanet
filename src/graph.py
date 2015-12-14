# The main graph object

__author__ = "David L Gibbs"
__project__ = "GraphPlanet"

from collections import OrderedDict
from scipy.sparse import coo_matrix
import numpy as np


class Graph:
    """ The main graph object. """

    def neighbors(self,vi):
        idx  = self.matidx[vi]
        nIdx = self.graph.getrow(idx).toarray().flatten()
        wIdx = np.where(nIdx)[0]
        return([self.nodeids[xi] for xi in wIdx])

    def getAllIns(self):
        # get node names with in edges
        tonodes = list(self.graph.col)
        return([self.nodeids[xi] for xi in tonodes])

    def getRow(self,vi):
        idx = self.matidx[vi]
        return(self.graph.getrow(idx))

    def getIdx(self,vi):
        return(self.matidx[vi])

    def getVs(self):
        return(self.nodeNames)

    def numVertices(self):
        return(self.nvertices)

    def numEdges(self):
        return(self.nedges)

    def addEdge(self,node1,node2):
        if node1 not in self.matidx:
            self.matidx[node1] = self.i
            self.i+=1
        if node2 not in self.matidx:
            self.matidx[node2] = self.i
            self.i+=1
        r = list(self.graph.row)
        c = list(self.graph.col)
        d = list(self.graph.data)
        r.append(node1)
        c.append(node2)
        d.append(1)
        self.nedges +=1
        self.nvertices += 1
        self.nodeNames.append(node1)
        self.nodeNames.append(node2)
        n = self.nvertices
        # UPDATE THE MATIDX AND INVERSE #
        self.graph = coo_matrix((d,(r,c)), shape=(n,n))

    def addEdgeWithWt(self,node1,node2,wt):
        if node1 not in self.matidx:
            self.matidx[node1] = self.i
            self.nvertices += 1
            self.i+=1
        if node2 not in self.matidx:
            self.matidx[node2] = self.i
            self.nvertices += 1
            self.i+=1
        r = list(self.graph.row)
        c = list(self.graph.col)
        d = list(self.graph.data)
        r.append(self.matidx[node1])
        c.append(self.matidx[node2])
        d.append(float(wt))
        self.nedges +=1
        n = self.nvertices
        # UPDATE THE MATIDX AND INVERSE #
        self.graph = coo_matrix((d,(r,c)), shape=(n,n))

    def remEdge(self, node1, node2):
        nodeidx1 = self.matidx[node1]
        nodeidx2 = self.matidx[node2]
        r = list(self.graph.row)
        c = list(self.graph.col)
        d = list(self.graph.data)
        idx = 0
        for ri, ci, di in zip(r,c,d):
            if ri == nodeidx1 and ci == nodeidx2:
                break
            idx+=1
        r = np.delete(r, idx)
        c = np.delete(c, idx)
        d = np.delete(d, idx)
        self.nedges -=1
        self.nvertices -= 1
        n = len(r)
        # UPDATE THE MATIDX AND INVERSE #
        self.graph = coo_matrix((d,(r,c)), shape=(n,n))

    def edgeList(self, filename):
        # HERE the file type is:  node  \t  node  \n
        # HERE the file type is:  node  \t  node  \t weight  \n
        text = open(filename,'r').read().strip().split("\n")
        edges  = map(lambda x: x.split(), text)
        self.i = 0  # the index
        self.matidx = dict()
        rows = []
        cols = []
        dats = []
        for node1, node2 in edges:
            rows.append(node1)
            cols.append(node2)
            dats.append(1)
            if node1 not in self.matidx:
                self.matidx[node1] = self.i
                self.i+=1
            if node2 not in self.matidx:
                self.matidx[node2] = self.i
                self.i+=1
        self.nedges = len(rows)
        self.nvertices = n = len(self.matidx)
        dats = map(float, dats)
        rowidx = [self.matidx[i] for i in rows]
        colidx = [self.matidx[i] for i in cols]
        self.nodeNames = self.matidx.keys()
        self.nodeids = {v: k for k, v in self.matidx.items()}
        self.graph = coo_matrix((dats,(rowidx,colidx)), shape=(n,n))

    def edgeListWithWeights(self, filename):
        # HERE the file type is:  node  \t  node  \t weight  \n
        text = open(filename,'r').read().strip().split("\n")
        edges  = map(lambda x: x.split(), text)
        self.i = 0  # the index
        self.matidx = dict()
        rows = []
        cols = []
        dats = []
        for node1, node2, wt in edges:
            rows.append(node1)
            cols.append(node2)
            dats.append(wt)
            if node1 not in self.matidx:
                self.matidx[node1] = self.i
                self.i+=1
            if node2 not in self.matidx:
                self.matidx[node2] = self.i
                self.i+=1
        self.nedges = len(rows)
        self.nvertices = n = len(self.matidx)
        dats = map(float, dats)
        rowidx = [self.matidx[i] for i in rows]
        colidx = [self.matidx[i] for i in cols]
        self.nodeids = {v: k for k, v in self.matidx.items()}
        self.nodeNames = self.matidx.keys()
        self.graph = coo_matrix((dats,(rowidx,colidx)), shape=(n,n))

    def sifList(self, filename):
        # HERE the file type is:  node  \t  node  \n
        text = open(filename,'r').read().strip().split("\n")
        edges  = map(lambda x: x.split(), text)
        rows = []
        cols = []
        data = []
        nods = []
        for node1, wt, node2 in edges:
            rows.append(node1)
            cols.append(node2)
            dats.append(wt)
            nods.append(node1)
            nods.append(node2)
        self.nedges = len(rows)
        self.nvertices = n = len(set(nods))
        self.nodeNames = list(set(nods))
        self.nodeids = {v: k for k, v in self.matidx.items()}
        self.nodeNames = self.matidx.keys()
        self.graph = coo_matrix((data,(rows,cols)), shape=(n,n))

    def __init__(self,name,type):
        self.type = type
        self.name = name
        self.nvertices = 0
        self.nodeNames = []
        self.nedges = 0

