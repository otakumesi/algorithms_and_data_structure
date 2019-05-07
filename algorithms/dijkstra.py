vertexs = set(['s', 'a', 'b', 'c', 'd', 'g'])
costs = {
    's': {
        'a': 2,
        'b': 9
    },
    'a': {
        'c': 3
    },
    'c': {
        'b': 3,
        'd': 8,
        'g': 9
    },
    'b': {
        'a': 7,
        'd': 2
    },
    'd': {
        'g': 1
    }
}

def dijkstra(vertexs, costs, start):
    cost_table = {}
    vertexs.remove(start)
    for vertex in vertexs:
        cost_table[vertex] = costs.get(start).get(vertex, 999)

    while bool(vertexs):
        w = get_path_min_cost_edge(cost_table, vertexs)
        vertexs.remove(w)
        for rest in vertexs:
            cost_table[rest] = min(cost_table[rest], cost_table[w] + costs.get(w).get(rest, 999))
    return cost_table

def get_path_min_cost_edge(cost_table, vertexs):
    rest_cost_table = { k:v for k, v in cost_table.items() if k in vertexs }
    return min(rest_cost_table, key=cost_table.get)

print(dijkstra(vertexs, costs, 's'))
