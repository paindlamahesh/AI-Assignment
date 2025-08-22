## output

Result (Best First Search):
Path length: 3 , Path: [(0, 0), (1, 1), (2, 2)]

Result (A* Search):
Path length: 3 , Path: [(0, 0), (1, 1), (2, 2)]

## ALGORITHM COMPARISON

Best-First Search is a greedy algorithm that expands the node it estimates is closest to the goal, using only a heuristic function (h(n)).
While it's fast, it is not guaranteed to find the optimal or shortest path because it ignores the cost already incurred.

A* Search is a more sophisticated algorithm that is both efficient and optimal. 
It evaluates nodes by combining the actual cost from the start node (g(n)) with the estimated cost to the goal (h(n)). 
This balanced approach ensures it finds the shortest path without getting stuck in locally optimal but globally suboptimal routes.


