graph = {
    'a': ['b'],
    'b': ['c', 'f'],
    'c': [],
    'd': ['a', 'e'],
    'e': ['f'],
    'f': ['c']
}

def depth_first_search(graph):
    visited = {}
    for v in graph.keys():
        visited[v] = False
    for vertex in graph.keys():
        dfs(vertex, graph, visited)

def dfs(vertex, graph, visited):
    if visited[vertex]:
        return
    visited[vertex] = True

    print(vertex)

    for path in graph[vertex]:
        dfs(path, graph, visited)

depth_first_search(graph)
