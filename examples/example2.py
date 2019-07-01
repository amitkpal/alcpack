#!/usr/bin/env python3

# Adaptive Local Complementation Package: Example 1
# @author: amitsweb
# 2019

# import the packages
import networkx as nx
import alcpack as alc


# edges and nodes in the graph
nodelist=list([1,2,3,4,5,6,7,8])
edgelist=list([(1,2),(1,3),(1,5),(1,8),(2,3),(2,4),(2,8),(3,4),(3,7),(4,5),(4,6),(5,6),(6,7),(6,8),(7,8)])

# build the graph
G=nx.Graph()
G.add_nodes_from(nodelist1)
G.add_edges_from(edgelist1)

# choose a path
path=list([1,2,3,4,5,6,7])

# apply path_category function
pc=alc.path_category(G,path)

print(pc[0]) # category of the path

print(pc[1]) # distilled path of category 1

# apply adaptive local complementation function
H=alc.alc_function(G,path)

# check if the edge (1,5) is in output graph H
print(sorted(list(H.edges())))
