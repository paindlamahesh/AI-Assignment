class State:
    def __init__(self, x, y, grid, goal):
        self.x = x
        self.y = y
        self.grid = grid
        self.goal = goal

    def goalTest(self):
        return (self.x, self.y) == self.goal

    def moveGen(self):
        n = len(self.grid)
        moves = [(-1,-1), (-1,0), (-1,1),
                 (0,-1),         (0,1),
                 (1,-1),  (1,0), (1,1)]
        children = []
        for dx, dy in moves:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < n and 0 <= ny < n and self.grid[nx][ny] == 0:
                children.append(State(nx, ny, self.grid, self.goal))
        return children

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x},{self.y})"


    def h(self):
        return abs(self.x - self.goal[0]) + abs(self.y - self.goal[1])

    def k_step_cost(self, other):
        return 1



def get_min_h(OPEN):
    best = OPEN[0]
    for node, path in OPEN:
        if node.h() < best[0].h():
            best = (node, path)
    return best

def get_min_f(OPEN, f):
    best = OPEN[0]
    for node in OPEN:
        if f[node] < f[best]:
            best = node
    return best



def best_first_search(start):
    if start.grid[0][0] == 1 or start.grid[-1][-1] == 1:
        return -1, []

    OPEN = [(start, [start])]
    visited = set()

    while OPEN:
        N, path = get_min_h(OPEN)
        OPEN.remove((N, path))

        if N in visited:
            continue
        visited.add(N)

        if N.goalTest():
            return len(path), [(s.x, s.y) for s in path]

        for M in N.moveGen():
            if M not in visited:
                OPEN.append((M, path + [M]))

    return -1, []



def a_star(start):
    if start.grid[0][0] == 1 or start.grid[-1][-1] == 1:
        return -1, []

    parent = {}
    g = {}
    f = {}

    OPEN = [start]
    CLOSED = set()

    parent[start] = None
    g[start] = 0
    f[start] = g[start] + start.h()

    while OPEN:
        N = get_min_f(OPEN, f)
        OPEN.remove(N)

        if N.goalTest():

            path = []
            while N:
                path.append(N)
                N = parent[N]
            path.reverse()
            return len(path), [(s.x, s.y) for s in path]

        CLOSED.add(N)

        for M in N.moveGen():
            if g[N] + N.k_step_cost(M) < g.get(M, float('inf')):
                parent[M] = N
                g[M] = g[N] + N.k_step_cost(M)
                f[M] = g[M] + M.h()

                if M not in CLOSED and M not in OPEN:
                    OPEN.append(M)

    return -1, []


grid=[[0,1,0],
      [0,0,1],
      [1,0,0]]
n=len(grid)
start_state = State(0, 0, grid, (n-1, n-1))

bfs_len, bfs_path = best_first_search(start_state)
astar_len, astar_path = a_star(start_state)

print("\nResult (Best First Search):")
if bfs_len == -1:
  print("Path length: -1 (No path exists)")
else:
  print("Path length:", bfs_len , ", Path:", bfs_path)
  # print("Path:", bfs_path)

print("\nResult (A* Search):")
if astar_len == -1:
  print("Path length: -1 (No path exists)")
else:
  print("Path length:", astar_len,", Path:", astar_path)
