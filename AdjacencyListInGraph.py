class Graph:
    def __init__(self):
        self.graph={}
        self.directed=False
    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def addEdge(self,src,dest):
        
        self.addVertex(src)
        self.addVertex(dest)

        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)
    def displaygraph(self):
        for vertex in self.graph:
            print(f"{vertex} ->{self.graph[vertex]}")

    def dfs(self,vertex,visited):
        if vertex not in visited:
            print(vertex,end=' ')
            visited[vertex]=True
            for v in self.graph[vertex]:
                self.dfs(v,visited)
  

    def bfs(self,startvertex):
        queue=[startvertex]
        visited={startvertex:True}
        while queue:
            currentvertex=queue.pop(0)
            print(currentvertex,end=" ")
            for i in self.graph[currentvertex]:
                if i not in visited:
                    queue.append(i)
                    visited[i]=True
        



    

A=Graph()
A.addEdge('A','B')
A.addEdge('A','D')
A.addEdge('A','C')
A.addEdge('C','D')
A.addEdge('D','E')
A.addEdge('C','F')
A.addEdge('E','F')
A.addEdge('D','B')

A.displaygraph()
A.dfs('A',{})
print()
A.bfs('A')