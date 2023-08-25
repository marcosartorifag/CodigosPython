# DFS - Algoritmo para busca em profundidade

# Função para imprimir a DFS do grafo recebe o primeiro nó a ser visitado
def dfs(graph, start, ponto_final):
    visited = set()  # Conjunto para acompanhar os nós visitados
    stack = [start]  # Pilha para a busca em profundidade

    while stack:

        node = stack.pop()  # Pega o próximo nó da pilha
        if node not in visited:
            # print(node, end=" ")  # Processa o nó (aqui, apenas imprimimos)
            visited.add(node)    # Marca o nó como visitado
            # Adiciona vizinhos não visitados à pilha
            stack.extend(graph[node] - visited)
            print(f"passando por {node}")
        if node == ponto_final: 
            print("finalizando...")
            break; 


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
end_node = 'F'

print("Resultado da busca em profundidade:")
dfs(graph, start_node, end_node)
