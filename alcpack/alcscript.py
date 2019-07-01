#!/usr/bin/env python3

# Adaptive Local Complementation Package
# @author: amitsweb
# 2019




# based on NetworkX
import networkx as nx
#


# format of an edge in the graph
def link_format(x,y):
    l=sorted(list([x,y]))
    link=(l[0],l[1])
    return link
#


# determination of category of a path
# distillation of a category 1 path from a category 2 path
def path_category(G,path):
    A=nx.Graph(G)
    pc=1
    newpath=list([])
    for i in range(len(path)):
        if i==0:
           a=path[i]
        newpath.append(a)
        if a==path[-1]:
           break
        for j in reversed(range(path.index(a)+1,len(path))):
            link=link_format(a,path[j])
            if link in A.edges():
               if j>path.index(a)+1:
                  pc=2
               a=path[j]
               break
    return pc,newpath
#



# local complementation on a single target qubit
def local_complementation(G,target):
    A=nx.Graph(G)
    A_target=nx.ego_graph(A,target,1,center=False)
    A.remove_edges_from(list(A_target.edges()))
    A_target_comp=nx.complement(A_target)
    A=nx.compose(A,A_target_comp)
    H=nx.Graph(A)
    return H
#


# adaptive local complementation function 
def alc_function(G,path):
    if len(path)<=2:
       raise ValueError('Number of  edges in path should be more than one! Returning original graph..')
       H=nx.Graph(G)
    else:
       ab_link=link_format(path[0],path[-1])
       if ab_link not in list(G.edges()):
          if len(path)>3:
             pcv=path_category(nx.Graph(G),list(path))
             if pcv[0]==1:
                newpath=list(path)
             else:
                newpath=list(pcv[1])
          else:
             newpath=list(path)
          H=nx.Graph(G)
          for i in range(1,len(newpath)-1):
              glc=local_complementation(nx.Graph(H),newpath[i])
              H=nx.Graph(glc)
       else:
          raise ValueError('Link already exists! Returning original graph..')
          H=nx.Graph(G)
    return H
#
