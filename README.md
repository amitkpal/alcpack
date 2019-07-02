# `ALCPack`

A python package to create an edge between any two given nodes in a simple, connected, and undirected graph via a sequence of local complementation operations.


## Requirements

`ALCPack` is developed based on [**Python 3.0**](https://www.python.org/download/releases/3.0/) (or more recent releases), and uses [**NetworkX**](https://networkx.github.io) -- A python package to analyze complex networks


## Installation

To install `ALCPack` using [**pip**](https://pip.pypa.io/en/stable/):

>
>$ python3 -m pip install --upgrade pip
>
>$ python3 -m pip install alcpack
>

The steps to build the package locally for installation via [**pip**](https://pip.pypa.io/en/stable/) are given in **ALCPack_References**, available in the ***documentation*** folder. 


## Description 

`ALCPack` provides three functions, as listed below.

1. **local_complementation**(G, target): *Performs a local complementation operation on the input graph G w.r.t. the node 'target' and returns the transformed graph* 

2. **path_category**(G, path): *Determines the category of a simple path connecting two chosen nodes in a simple, connected, and undirected graph, and distills a category 1 path out of the chosen path, if the chosen path is of category 2. Returns the category (category 1 or category 2) of the chosenn path, and a distilled category 1 path (chosen path) if the chosen path is of category 2 (category 1)*  

3. **alc_function**(G, path): *Performs adaptive local complementation operation on the input graph G w.r.t. the chosen simple path 'path'. Returns the modified graph with an edge between the source and the destination nodes*  


## Use

To call `ALCPack` functions in the Python 3.0 (or higher) environment, 

>\>\>\> import alcpack as alc

To use `ALCPack` functions in the Python 3.0 (or higher) environment, 

>
>\>\>\> H=alc.local_complementation(G,target)
>
>\>\>\> n,newpath=alc.path_category(G,path)
>
>\>\>\> H=alc.alc_function(G,path)
>

The parameters used in the functions are as below.

**Input**

>
>**G**: Networkx graph, Input parameter
>


>
>**path**: List of nodes, Input parameter
>
>Represents a path between a source (first node in 'path') and a destination (last node in 'path')
>
 
> 
>**target**: Node, Input parameter
>
>Represents a node with respect to which the local complementation operation is performed
>


**Output**        
   
>   
>**H**: NetworkX graph, Output parameter
>
>Transformed graph due to ALCPack functions
>

>
>**n**: Integer, Output parameter 
>
>Takes value 1 or 2, represents the category of the input 'path'
>

>
>**newpath**: List of nodes, Output parameter
>
>Category 1 path
>
         
        
Information on the theoretical background of `ALCPack` is given in  **ALCPack_References**, which is available in the ***documentation*** folder. 
