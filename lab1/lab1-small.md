```python
from heuristicsearch.a_star_search import AStar

graph_nodes = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

heuristics = {'A':1, 'B':1, 'C':1, 'D':1}

graph= AStar(graph_nodes,heuristics)
graph.apply_a_star(start='A',stop='D')
```