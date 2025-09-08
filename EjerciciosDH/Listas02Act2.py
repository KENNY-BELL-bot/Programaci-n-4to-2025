# Lista de puntajes inicial 
puntajes = [850, 920, 670, 750, 830, 1000]
minimo = min(puntajes)
maximo = max(puntajes)
promedio = sum(puntajes)/len(puntajes)
puntajes.reverse()
print(puntajes)
puntajes.sort()
print("El TOP SCORE final es: " )
print(puntajes)