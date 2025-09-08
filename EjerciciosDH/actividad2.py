import datetime

# variables
ahora = datetime.datetime.now()
fecha = datetime.datetime(2010,3,30)
diferencia = ahora - fecha
diferenciaEnDias = diferencia.days
anios = diferenciaEnDias / 365
# prints
print(str(ahora))
print(fecha)
print(diferencia)
print(anios)

print("Tengo "+str(anios)+" años")