from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, start_vertex):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = True
        
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")  
            
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

def main():
    g = Graph()
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(0, 4)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 1)
    
    start_vertex = int(input("Digite o vértice de início da busca: "))
    
    print("Executando BFS, começando pelo vértice", start_vertex)
    g.BFS(start_vertex)

if __name__ == "__main__":
    main()
