import math
import heapq

def distancia_euclidiana(ponto1, ponto2, real=True):
    #Calcula a distância euclidiana entre dois pontos."""
    x1, y1 = ponto1[0], ponto1[1]
    x2, y2 = ponto2[0], ponto2[1]
    if real:
        return math.sqrt(math.pow(float(x1) - float(x2), 2) + math.pow(float(y1) - float(y2), 2))
    return math.sqrt(math.pow(int(x1) - int(x2), 2) + math.pow(int(y1) - int(y2), 2))

def peso_adicional_por_pedagio(grafo, ponto1, ponto2, limiar, peso):
    #Retorna um certo peso, caso determinado caminho esteja abaixo do limiar. 
    #Caso a aresta esteja abaixo do limiar isso indica que existe um pedagio na aresta em questão 
    if grafo[ponto1][ponto2] <= limiar:
        return peso
    else:
        return 0

def busca_a_estrela(grafo, inicio, fim):
    #Realiza a busca A* em um grafo para encontrar o caminho mais curto entre o nó de início e o nó final."""
    fronteira = []
    heapq.heappush(fronteira, (0, inicio))  # Adiciona o nó de início à fronteira com uma prioridade de 0
    visitados = set()  # Conjunto de nós já visitados
    antecessores = {}  # Dicionário que guarda os antecessores de cada nó no caminho
    custos = {}  # Dicionário que guarda o custo do caminho até cada nó

    antecessores[inicio] = None
    custos[inicio] = 0

    while fronteira:
        _, atual = heapq.heappop(fronteira)  # Remove o nó com a menor prioridade da fronteira
        if atual == fim:
            # Chegamos ao nó final, então encontramos o caminho
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = antecessores[atual]
            caminho.reverse()
            return caminho, custos, antecessores

        visitados.add(atual)

        # Para cada vizinho do nó atual, calcula o custo total do caminho até ele (g) e a heurística (h)
        for vizinho in grafo[atual]:
            if vizinho in visitados:
                continue
            g = custos[atual] + grafo[atual][vizinho]
            h1 = distancia_euclidiana(grafo['espaco'][vizinho], grafo['espaco'][fim], real=False)
            h2 = peso_adicional_por_pedagio(grafo, atual, vizinho, 3, 10)
            f = g + h1 + h2
            # Adiciona o vizinho à fronteira com a prioridade f
            heapq.heappush(fronteira, (f, vizinho))

            # Atualiza os antecessores e custos se encontramos um caminho melhor para o vizinho
            if vizinho not in custos or g < custos[vizinho]:
                antecessores[vizinho] = atual
                custos[vizinho] = g

    # Se chegamos aqui, não foi possível encontrar um caminho
    print("Não foi possivel encontrar um caminho")


grafo = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 3, 'D': 4},
    'C': {'A': 1, 'B': 3, 'D': 1, 'E': 5},
    'D': {'B': 4, 'C': 1, 'E': 4},
    'E': {'C': 5, 'D': 4},
    'espaco': {
        'A': (2,3),
        'B': (4,2),
        'C': (4,5),
        'D': (6,2),
        'E': (7,4)
    }
}

inicio = 'A'
fim = 'E'

caminho, custos, antecessores = busca_a_estrela(grafo, inicio, fim)
print(f"**Resultado**\n Camino: {caminho}\n", 
      f"Custos: {custos}\n", 
      f"Antecessores: {antecessores}"
      )