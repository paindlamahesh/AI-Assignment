class State:
    def __init__(self, init):
        self.init = init
        self.final = ['R', 'R', 'R', '_', 'L', 'L', 'L']

    def goalTest(self):
        return self.init == self.final

    def moveGen(self):
        children = []
        for i in range(len(self.init)):
            if self.init[i] == 'L':
                # Move right
                if i + 1 < len(self.init) and self.init[i + 1] == '_':
                    new_config = self.init[:]
                    new_config[i], new_config[i + 1] = new_config[i + 1], new_config[i]
                    children.append(State(new_config))
                # Jump over R
                if i + 2 < len(self.init) and self.init[i + 1] == 'R' and self.init[i + 2] == '_':
                    new_config = self.init[:]
                    new_config[i], new_config[i + 2] = new_config[i + 2], new_config[i]
                    children.append(State(new_config))

            elif self.init[i] == 'R':
                # Move left
                if i - 1 >= 0 and self.init[i - 1] == '_':
                    new_config = self.init[:]
                    new_config[i], new_config[i - 1] = new_config[i - 1], new_config[i]
                    children.append(State(new_config))
                # Jump over L
                if i - 2 >= 0 and self.init[i - 1] == 'L' and self.init[i - 2] == '_':
                    new_config = self.init[:]
                    new_config[i], new_config[i - 2] = new_config[i - 2], new_config[i]
                    children.append(State(new_config))

        return children

    def __eq__(self, other):
        return isinstance(other, State) and self.init == other.init

    def __hash__(self):
        return hash(tuple(self.init))

    def __repr__(self):
        return ''.join(self.init)


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

    path_str = " <- \n".join(str(state) for state in path)
    print("Goal is found\n" + path_str)
    return path


def bfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair
        if N.goalTest():
            return reconstructPath(node_pair, CLOSED)
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN.extend(new_pairs)
    return []


def dfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair
        if N.goalTest():
            return reconstructPath(node_pair, CLOSED)
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN = new_pairs + OPEN
    return []


if __name__ == "__main__":
    initial_config = ['L', 'L', 'L', '_', 'R', 'R', 'R']
    start_state = State(initial_config)

    print("\nRunning DFS on Rabbit Leap Problem:")
    dfs(start_state)

    print("\nRunning BFS on Rabbit Leap Problem:")
    bfs(start_state)
