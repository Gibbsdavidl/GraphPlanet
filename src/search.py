
# exporatory functions #

from collections import deque
from lexset import *
from copy import deepcopy

def dfs(g, vi):
    """
    :param g: graph object, unweighted
    :param v: vertex name
    :return:  list of vertex names
    """
    return(dfs_work(g,vi,[]))


def dfs_work(g, vi, discovered):
    discovered.append(vi)
    for vj in g.neighbors(vi):
        if vj not in discovered:
            dfs_work(g, vj, discovered)
    return(discovered)



def bfs(g, vi, wanted):
    """
    :param g: graph obj, unweighted
    :param v: vertex name
    :return:  list of vertex names
    """
    q = deque([vi])
    s = set(vi)
    while len(q) > 0:
        vi = q.popleft()
        if wanted(vi): # has some property
            return(vi)
        for vj in g.neighbors(vi):
            if vj not in s:
                q.append(vj)
                s.add(vj)
    return('not found')


def lexBfs(g):
    """
    :param g: graph
    :param vi: vertex to start with
    :return:
    """
    n = g.numVertices()
    vs = LexSet(g.getVs())
    q = deque([vs])             # build a queue of sets
    res0 = []                         # output of ordered vertices
    for i in range(n):                # while we have sets to process
        vi = q[0].lexpop()                # get out the first node, a lexset
        res0.append(vi)                   # append it to results
        for j in range(len(q)):           # for each set
            ns = g.neighbors(vi)              # get neighbors of vi
            si = q.popleft().toset()          # get out a lexset, might be empty
            s1 = si.intersection(ns)          # the nodes that are also neighbors
            s2 = si.difference(ns)            # the nodes that are not neighbors
            if len(s1) > 0: q.append(LexSet(s1))  # put 'em back, neighbors out
            if len(s2) > 0: q.append(LexSet(s2))
    return res0


def outOnly(g):
    vs  = set(g.getVs())
    ins = set(g.getAllIns())
    return(list(vs.difference(ins)))

def toposort(g):
    g2 = deepcopy(g)
    l = []             # will be the sorted list
    s = outOnly(g2)     # set of nodes with no incoming edges, out only
    while len(s) > 0:
        si = s.pop()   # take the first one off
        l.append(si)   # and append it to the results
        for m in g2.neighbors(si):  # for the neighbors of si
            g2.remEdge(si, m)       # remove edge from si to m
            if m not in g2.getAllIns():  # if m has incoming edges
                l.append(m)              # then put it in the solution
    if g.hasEdges():
        return("error")
    else:
        return(l)
