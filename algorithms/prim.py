graph = set(['a', 'b', 'c', 'd', 'e', 'f'])
costs = {
    tuple(set(['a', 'b'])): 1,
    tuple(set(['a', 'c'])): 3,
    tuple(set(['a', 'd'])): 8,
    tuple(set(['b', 'c'])): 4,
    tuple(set(['b', 'e'])): 5,
    tuple(set(['c', 'd'])): 9,
    tuple(set(['c', 'e'])): 6,
    tuple(set(['c', 'f'])): 7,
    tuple(set(['d', 'f'])): 2,
    tuple(set(['e', 'f'])): 10
}

def prim(graph, costs):
    s = 'a'
    graph.remove(s)

    cost_table ={}
    nexts = {}

    for v in graph:
        cost_table[v] = costs.get(tuple(set([s, v])), 999)
        nexts[v] = s

    tree = []

    while bool(graph):
        w = get_min_cost_vertex(graph, cost_table)
        graph.remove(w)

        tree.append((w, nexts[w]))
        for v in graph:
            if cost_table[v] > costs.get(tuple(set([w, v])), 999):
                cost_table[v] = costs.get(tuple(set([w, v])))
                nexts[v] = w

    return tree

def get_min_cost_vertex(graph, cost_table):
    rest_cost_table = { k:v for k, v in cost_table.items() if k in graph }
    return min(rest_cost_table, key=rest_cost_table.get)

print(prim(graph, costs))
