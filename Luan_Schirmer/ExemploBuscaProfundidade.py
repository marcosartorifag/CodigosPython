def verificar_alcance(objetivo, grafo, no_atual):
    fila = [no_atual]
    visitados = set()

    while fila:
        no = fila.pop(0)
        if no in visitados:
            continue
        
        visitados.add(no)
        
        if no == objetivo:
            return True
        
        fila.extend(grafo[no])
    
    return False

def main():
    grafo = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }
    
    objetivo = input("Digite o nó objetivo: ")
    no_inicial = input("Digite o nó inicial: ")
    
    alcancou_objetivo = verificar_alcance(objetivo, grafo, no_inicial)
    
    if alcancou_objetivo:
        print("O objetivo foi alcançado!")
    else:
        print("O objetivo não foi alcançado.")

if __name__ == "__main__":
    main()
