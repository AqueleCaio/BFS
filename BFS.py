def BFS(listaAdj, v):
    fila = []
    visitados = []
    
    for v in listaAdj:
        if v not in visitados:
            fila.append(v)
            
            while len(fila) > 0:
                v = fila.pop(0)
                
                if v not in visitados:
                    visitados.append(v)
                    
                    for u in listaAdj[v]:
                        fila.append(u)  
                
    print(visitados)

