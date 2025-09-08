# PV DEL DRAGON (en ingles)
puntos_vida_dragon = 100
# RANDOM
import random 
# LA MEGA FUNCION
def tirarDado (lados):
  return random.randint(1,lados)
# ATAQUE
def atacarDragon():
  ataque = tirarDado(20)+tirarDado(4)
  return ataque
# NO SE
puntos_vida_dragon = puntos_vida_dragon - atacarDragon()
# FIN
print("Los puntos de vida del dragón son: "+str(puntos_vida_dragon))