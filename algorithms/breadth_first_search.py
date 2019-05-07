graph = {
    'a': ['b'],
    'b': ['c', 'f'],
    'c': [],
    'd': ['a', 'e'],
    'e': ['f'],
    'f': ['c']
}

def breadth_first_search(graph):
    visited = {}
    for v in graph.keys():
        visited[v] = False
    for vertex in graph.keys():
        bfs(vertex, graph, visited)

def bfs(vertex, graph, visited):
    queue = []
    queue.append(vertex)

    while bool(queue):
        v = queue.pop()

        if not visited[v]:
            visited[v] = True

            print(v)

            for u in graph[v]:
                queue.append(u)

breadth_first_search(graph)
