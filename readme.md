Shortest Path
=============

An exploration of searching graphs for a shortest path

![Shortest path example](https://upload.wikimedia.org/wikipedia/commons/2/23/Dijkstras_progress_animation.gif)

Learning Objectives
-------------------

After completing this lab, students will be able to:

- Implement graph search algorithms in Python
- Understand the costs and benefits of breadth-first, depth-first, and Dijkstra's algorithm

Task
----

Examine the included graph data in [nodes.csv](nodes.csv) and [edges.csv](edges.csv). Handout code is provided to load, process, and display this data in [search.py](search.py)

Implement `search_depth_first`, `search_dijkstra`, and `search_breadth_first` so that all included tests pass.

Tools
-----

The handout code does not produce any graphical output by default, but if you'd like to view particular paths, you can call the `show_path` method to produce a plot using matplotlib. If used correctly, a path should be shown that looks something like this:

![DFS example](media/dfs.png)
