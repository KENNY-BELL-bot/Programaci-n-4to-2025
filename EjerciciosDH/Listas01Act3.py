frutas = ["pistacho", "Mandarina", "Patata", "Naranja", "Pomelo", "Coco", "Tomate", "Kiwi", "Mango", "Cebolla"]
frutas[2] = "Fresa"
frutas[6] = "Manzana"
frutas[9] = "Durazno"
frutas.sort()
print(frutas)
if "maracuyá" in frutas:
  print("Sí, hay maracuyá")
else:
  print("No hay maracuyá")
frutas.reverse()
print(frutas)