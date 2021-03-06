import modelagens as m
import heapq

def gulosa(arvore,node_inicio,objetivo):
    fila = []
    heapq.heappush(fila,(arvore[node_inicio]['h'],(node_inicio,[node_inicio],0)))
    nos_visitados =[]
    while fila:
        expande = []
        expande.append(heapq.heappop(fila))
        (pai,caminho,custo) =expande[0][1]
        nos_visitados.append(pai)
        if pai == objetivo:
            resultado = {'caminho': caminho,'custo':custo,'nos_visitados':nos_visitados}
            return resultado 
        
        filhos = arvore[pai]['filhos']
        for filho in filhos:
            custo_acc = custo + arvore[filho]['custos'][pai]
            heapq.heappush(fila,(arvore[filho]['h'],(filho,caminho + [filho],custo_acc)))


# result = gulosa(m.ilustracao_a,'A','H')
result = gulosa(m.ilustracao_b,'A','L')

result_formatado = {
    'caminho ({})'.format(len(result['caminho'])): result['caminho'],
    'custo' : result['custo'],
    'nos_visitados ({})'.format(len(result['nos_visitados'])): result['nos_visitados']
}

print('Guloso: ',result_formatado)