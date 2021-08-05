# python-delaunay
A Python implementation of Delaunay triangulation. This implements a naive algorithm to generate valid Delaunay triangulations of a set of points. A triangulation is considered to be a Delaunay triangulation when, for any triangle in the set of points, the circumcircle of that triangle does not contain any other data points. More information about Delaunay triangulations can be found here: https://en.wikipedia.org/wiki/Delaunay_triangulation

The algorithm for generating the Delaunay mesh is very inefficient and runs in O(N^3) time. This can be greatly improved by the use of an incremental algorithm such as Bowyer-Watson (https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm), which can run in O(N log N) time. 

The demo included in this repository uses PyGame (https://www.pygame.org/) to display the final triangulation. While this may not necessarily be the best choice, it was simpler for me because of previous experience with PyGame, so I was able to focus on the core part of the project without having to worry about learning matplotlib or some other extension, at least for the moment. The python_delaunay.py file which contains the mesh generation algorithm does not rely on PyGame.

An example triangulation of random points:
![A Delaunay Triangulation](https://github.com/abbottjord94/python-delaunay/blob/main/delaunay.png)
