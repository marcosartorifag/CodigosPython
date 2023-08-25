# BFS - Algoritmo para Busca em Largura

# Importa a biblioteca para poder criar uma lista
from collections import defaultdict

# classe para criação do grafo direcionado e que usa representação de lista de adjacência


class Graph:

    # constroi a função que ira criar a lista
    def __init__(self):
        # Quando você cria um defaultdict, fornece uma função usada para criar valores, nesse caso criou-se a lista
        self.graph = defaultdict(list)

    # função que adiciona os vértices no grafo
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # função para imprimir a BFS do grafo recebe o primeiro nó a ser visitado
    def BFS(self, s, ponto_final):

        # marca todos os vértices como não visitados.
        visited = [False] * (len(self.graph))

        # cria uma fila vazia para o BFS
        queue = []

        # pega o nó de origem, marca como visitado e insere ele na fila
        queue.append(s)
        visited[s] = True

        # enquanto a fila não for vazia
        while queue:

            # retira o último vértice inserido na fila e imprime
            s = queue.pop(0)  # Exclui valor e printa a resposta
            # print(s, " ")
            print(f"O valor {s} foi visitado")
            if (s == ponto_final):
                print("finalizando...")
                break

            # Obtenha todos os vértices adjacentes dos vértices desenfileirados. Se um adjacente não foi visitado, marque-o como visitado e coloque-o na fila
            # quais vértices eu posso visitar a partir do atual? Sempre do menor pro maior.
            for i in self.graph[s]:
                # print(visited[i])
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Criação do grafo
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

print("Segue a execução do BFS, começando pelo vértice 0")

# recebe ponto de partida (s) e ponto final
g.BFS(1, 4)