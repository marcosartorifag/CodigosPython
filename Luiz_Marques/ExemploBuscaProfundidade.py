# DFS - Algoritmo para busca em profundidade

# Função para imprimir a DFS do grafo recebe o primeiro nó a ser visitado
def dfs(graph, start, objective):
    visited = set()  # Conjunto para acompanhar os nós visitados
    stack = [start]  # Pilha para a busca em profundidade

    while stack:

        node = stack.pop()  # Pega o próximo nó da pilha
        if objective == node:
            print(node)
            print("Você chegou no objetivo")
            break

        if node not in visited:
            print(node, end=" ")  # Processa o nó (aqui, apenas imprimimos)
            visited.add(node)    # Marca o nó como visitado
            # Adiciona vizinhos não visitados à pilha
            stack.extend(graph[node] - visited)

        

# Exemplo de um grafo representado como um dicionário de adjacências
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

start_node = 'A'  # Nó de início da busca
print("Informe a letra do objetivo (a, b, c, d, e ou f)")
object_node = input(str).upper() 

if str(object_node) in ('A', 'B', 'C', 'D', 'E', 'F'):
    print("Resultado da busca em profundidade:")
    dfs(graph, start_node, object_node)
else:
    print("Letra informada é inválida")
