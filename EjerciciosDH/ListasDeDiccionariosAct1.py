jugadores = []

contador = 1

while contador <= 3:
    nombre = input("Ingrese el nombre del jugador " + str(contador) + ": ")
    apellido = input("Ingrese el apellido del jugador " + str(contador) + ": ")
    edad = input("Ingrese la edad del jugador " + str(contador) + ": ")
    club1 = input("Ingrese el primer club del jugador " + str(contador) + ": ")
    club2 = input("Ingrese el segundo club del jugador " + str(contador) + ": ")

    jugador = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "club1": club1,
        "club2": club2
    }

    jugadores.append(jugador)

    
    contador += 1

indice = 1
for jugador in jugadores:
    print("Los datos del jugador " + str(indice) + " son: " +
          jugador["nombre"] + " " + jugador["apellido"] +
          ", Edad: " + jugador["edad"] +
          ", Clubes: " + jugador["club1"] + " y " + jugador["club2"])
    indice += 1