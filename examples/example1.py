#!/usr/bin/env python3

# Adaptive Local Complementation Package: Example 1
# @author: amitsweb
# 2019

# import the packages
import networkx as nx
import alcpack as alc


# edges and nodes in the graph
nodelist=list([1,2,3,4,5,6,7,8,9])
edgelist=list([(1,2),(1,8),(1,9),(2,3),(2,9),(3,4),(3,9),(4,5),(4,9),(5,6),(5,9),(6,7),(6,9),(7,8),(7,9),(8,9)])

# build the graph
G=nx.Graph()
G.add_nodes_from(nodelist1)
G.add_edges_from(edgelist1)

# choose a path
path=list([1,2,9,4,5])

# apply path_category function
pc=alc.path_category(G,path)

print(pc[0]) # category of the path

print(pc[1]) # distilled path of category 1

# apply adaptive local complementation function
H=alc.alc_function(G,path)

# check if the edge (1,5) is in output graph H
print(sorted(list(H.edges())))
