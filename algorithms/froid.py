vertexs = set(['a', 'b', 'c', 'd'])
costs = {
    'a': {
        'b': 2,
        'c': 6,
        'd': 9
    },
    'b': {
        'c': 3
    },
    'c': {
        'd': 1,
    },
    'd': {
        'a': 2
    }
}

def froid(vertexs, costs):
    cost_table = {}
    for v in vertexs:
        cost_table[v] = {}
        rests = vertexs.copy()
        rests.remove(v)
        for u in rests:
            cost_table[v][u] = costs.get(v).get(u, 999)

    for v in vertexs:
        rests = vertexs.copy()
        rests.remove(v)
        while bool(rests):
            w = get_min_cost_path(cost_table, v, rests)
            rests.remove(w)

            for r in rests:
                cost_table[v][r] = min(cost_table[v][r], cost_table[v][w] + costs[w].get(r, 999))

    return cost_table



def get_min_cost_path(cost_table, current_vertex, vertexs):
    rest_cost_table = { k:v for k,v in cost_table[current_vertex].items() if k in vertexs }
    return min(rest_cost_table, key=rest_cost_table.get)

print(froid(vertexs, costs))
