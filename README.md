# `ALCPack`

A python package to create an edge between any two given nodes in a simple, connected, and undirected graph via a sequence of local complementation operations.

### Requirements

`ALCPack` is developed based on [**Python 3.0**](https://www.python.org/download/releases/3.0/) (or more recent releases), and uses [**NetworkX**](https://networkx.github.io) -- A python package to analyze complex networks



### Installation

To install `ALCPack` using [**pip**](https://pip.pypa.io/en/stable/):

>
>$ python3 -m pip install --upgrade pip
>
>$ python3 -m pip install alcpack
>


The steps to build the package locally for installation via [**pip**](https://pip.pypa.io/en/stable/) are given in [**ALCPack_References**](documentation/alcpack_references.pdf), available in the *documentation* folder. 


### Use

To call `ALCPack` functions in the Python 3.0 (or higher) environment, 

>\>\>\> import alcpack as alc


### Description 

ALCPack provides three functions, as listed below.

1. **local_complementation**(G,target): *Performs a local complementation operation on the input graph G w.r.t. the node 'target' and returns the transformed graph* 
2. **path_category**(G,path): *Determines the category of a simple path connecting two chosen nodes in a simple, connected, and undirected graph, and distills a category 1 path out of the chosen path, if the chosen path is of category 2. Returns the category (category 1 or category 2) of the chosenn path, and a distilled category 1 path (chosen path) if the chosen path is of category 2 (category 1) *  
3. **alc_function**(G,path): *Adaptive local complementation operation on the input graph G w.r.t. the chosen simple path 'path'. Returns the modified graph with an edge between the source and the target nodes*  

Details of the functions along with essential background information and comprehensive examples are availale in  [**ALCPack_References**](documentation/alcpack_references.pdf). 


### Citation
```
@article{amaro2019,
  author = 	"David Amaro and Markus Müller and Amit Kumar Pal",
  title = 	"Scalable characterization of localizable entanglement in noisy topological quantum codes",
  year = 	"2019",
  month =   "July"
}
```
