import heapq
vertexs = ['a', 'b', 'c', 'd', 'e', 'f']

edges = [
  (1, set(['a', 'b'])),
  (3, set(['a', 'c'])),
  (8, set(['a', 'd'])),
  (4, set(['b', 'c'])),
  (5, set(['b', 'e'])),
  (9, set(['c', 'd'])),
  (6, set(['c', 'e'])),
  (7, set(['c', 'f'])),
  (2, set(['d', 'f'])),
  (10, set(['e', 'f']))
]

class Graph:
    def __init__(self, nodes=None, edges=None):
        if nodes != None:
            self.nodes = set(nodes)
        else:
            self.nodes = set([])

        if edges != None:
            self.edges = set(edges)
        else:
            self.edges = set([])

    def push_node(self, node):
        self.nodes.add(node)

    def push_edge(self, edge):
        self.edges.add(edge)

    def __eq__(self, value):
        return value.nodes == self.nodes

    def merge(self, other, edge):
        self.nodes = self.nodes.union(other.nodes)
        self.edges = self.edges.union(other.edges)
        self.edges.add(tuple(edge))
        return self

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        return "<Graph: {} and {}>".format(str(self.nodes), str(self.edges))

def kruscal(vertexs, edges):
    queue = []
    for edge in edges:
        heapq.heappush(queue, edge)

    graphs = [Graph(vertex) for vertex in vertexs]

    while bool(queue):
        edge = heapq.heappop(queue)[1]
        tree_left, tree_right = get_trees_from_edge(edge, graphs)

        if tree_left != tree_right:
            graphs = [graph for graph in graphs if not any([graph.has_node(node) for node in edge])]
            graphs.append(tree_left.merge(tree_right, edge))

    return graphs[0]

def get_trees_from_edge(edge, trees):
    trees_from_edge = []
    for node in edge:
        trees_from_edge = trees_from_edge + [tree for tree in trees if tree.has_node(node)]
    return trees_from_edge

print(kruscal(vertexs, edges))
