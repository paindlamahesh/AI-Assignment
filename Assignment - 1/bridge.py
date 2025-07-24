class State:
    def __init__(self, left, right, umbrella_side, time_elapsed):
        self.left = left      # People on left side
        self.right = right    # People on right side
        self.umbrella = umbrella_side  # 'L' or 'R'
        self.time = time_elapsed       # Total time spent so far

    def goalTest(self):
        return len(self.left) == 0 and self.umbrella == 'R'

    def moveGen(self):
        children = []
        people = self.left if self.umbrella == 'L' else self.right

        # Generate all 1 or 2-person combinations
        for i in range(len(people)):
            for j in range(i, len(people)):
                p1 = people[i]
                p2 = people[j]
                crossing = [p1] if i == j else [p1, p2]

                new_left = self.left[:]
                new_right = self.right[:]
                new_side = 'R' if self.umbrella == 'L' else 'L'

                # Transfer people and update time
                if self.umbrella == 'L':
                    for p in crossing:
                        new_left.remove(p)
                        new_right.append(p)
                else:
                    for p in crossing:
                        new_right.remove(p)
                        new_left.append(p)

                crossing_time = max(crossing)
                new_time = self.time + crossing_time
                child = State(new_left, new_right, new_side, new_time)

                children.append(child)

        return children

    def __eq__(self, other):
        return isinstance(other, State) and \
               sorted(self.left) == sorted(other.left) and \
               sorted(self.right) == sorted(other.right) and \
               self.umbrella == other.umbrella

    def __hash__(self):
        return hash((tuple(sorted(self.left)), tuple(sorted(self.right)), self.umbrella))

    def __repr__(self):
        return f"Left: {self.left}, Right: {self.right}"


def removeSeen(children, OPEN, CLOSED):
    open_nodes = [node for node, _ in OPEN]
    closed_nodes = [node for node, _ in CLOSED]
    return [node for node in children if node not in open_nodes and node not in closed_nodes]


def reconstructPath(node_pair, CLOSED):
    parent_map = {node: parent for node, parent in CLOSED}
    node, parent = node_pair
    path = [node]
    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    path.reverse()
    print("\nSolution Path:")
    for step in path:
        print(step)
    print(f"\nTotal Time: {path[-1].time} minutes")


def bfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        node, parent = node_pair
        if node.goalTest():
            print("Goal Found!")
            return reconstructPath(node_pair, CLOSED)
        CLOSED.append(node_pair)
        children = node.moveGen()
        new_nodes = removeSeen(children, OPEN, CLOSED)
        new_pairs = [(child, node) for child in new_nodes]
        OPEN += new_pairs
    return []


def dfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        node, parent = node_pair
        if node.goalTest():
            print("Goal Found!")
            return reconstructPath(node_pair, CLOSED)
        CLOSED.append(node_pair)
        children = node.moveGen()
        new_nodes = removeSeen(children, OPEN, CLOSED)
        new_pairs = [(child, node) for child in new_nodes]
        OPEN = new_pairs + OPEN
    return []


# --- Test the BFS and DFS with 4 people ---
# Crossing times
Amogh = 5
Ameya = 10
Grandmother = 20
Grandfather = 25

initial_state = State(
    left=[Amogh, Ameya, Grandmother, Grandfather],
    right=[],
    umbrella_side='L',
    time_elapsed=0
)

print("Running BFS on Bridge and Umbrella Problem:")
bfs(initial_state)

print("\nRunning DFS on Bridge and Umbrella Problem:")
dfs(initial_state)
