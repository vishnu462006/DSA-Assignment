class Graph:
    def __init__(self):
        self.graph = {}
        self.directed = True  

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, src, dest):
        self.addVertex(src)
        self.addVertex(dest)
        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)

    def displaygraph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)

    def topologicalSort(self):
        visited = {key: False for key in self.graph}
        stack = []
        for vertex in self.graph:
            if not visited[vertex]:
                self.topologicalSortUtil(vertex, visited, stack)
        print(stack)


A = Graph()
A.addEdge('A', 'B')
A.addEdge('A', 'D')
A.addEdge('A', 'C')
A.addEdge('C', 'D')
A.addEdge('D', 'E')
A.addEdge('C', 'F')
A.addEdge('E', 'F')
A.addEdge('D', 'B')

A.displaygraph()
A.topologicalSort()
