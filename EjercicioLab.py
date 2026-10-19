def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c):
    if f >= len(lab) or f < 0:
        return False
    if c >= len(lab[0]) or c < 0:
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True

def laberB_Puntos(lab, res, f, c, puntos_actuales):

    if not valido(lab, res, f, c):
        return False
    valor_celda = lab[f][c]
    if valor_celda == 'I' or valor_celda == 'F':
        puntos_actuales = puntos_actuales + 1
    else:
        puntos_actuales = puntos_actuales + valor_celda
    res[f][c] = 1

    if f == 0 and c == 0:
        if puntos_actuales >= 23:
            print("******* ¡CAMINO VIABLE ENCONTRADO! ********")
            print("Puntaje total obtenido en esta ruta:", puntos_actuales)
            return True
        else:
            res[f][c] = 0
            return False
    #movernos hacia arriba 
    if laberB_Puntos(lab, res, f - 1, c, puntos_actuales):
        return True
        
    #movernos hacia la derecha 
    elif laberB_Puntos(lab, res, f, c + 1, puntos_actuales):
        return True
        
    #movernos hacia abajo 
    elif laberB_Puntos(lab, res, f + 1, c, puntos_actuales):
        return True
        
    # movernos hacia la izquierda 
    elif laberB_Puntos(lab, res, f, c - 1, puntos_actuales):
        return True
    res[f][c] = 0
    return False

laberinto = [
    ['F', 1,  1,  3,  0,  1,  1,  1,  4],
    [ 3,  0,  0,  1,  0,  1,  0,  0,  1],
    [ 1,  1,  0,  1,  1,  1,  1,  0,  1],
    [ 0,  1,  0,  1,  4,  3,  1,  1,  0],
    [ 1,  1,  1,  1,  1,  1,  3,  1,  1],
    [ 3,  0,  1,  0,  0,  0,  1,  0,  1],
    [ 1,  1,  1,  1,  3,  1,  1,  1,  1],
    [ 1,  0,  0,  1,  0,  1,  0,  0,  4],
    ['I', 1,  3,  1,  0,  1,  1,  1,  1]
]

res = []
for i in range(9):
    fila = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    res.append(fila)


print("********LABERINTO INICIAL !ENCUENTRA LA SALIDA RATONCITO!********")
imprime(laberinto)
# Para iniciar en la parte inferior izquierda .
if laberB_Puntos(laberinto, res, 8, 0, 0):
    print("¡Salimos con el puntaje requerido ratoncito!")
    print("\n*********MATRIZ DE SOLUCIÓN (CAMINO TOMADO) *******")
    imprime(res)
    print("Salimos!!!!!")
else:
    print("Quedamos atrapados o ningún camino válido sumo mas de 23 puntos.")
    print("\n*********MATRIZ DE SOLUCIÓN (CAMINO TOMADO) *******")
    imprime(res)

