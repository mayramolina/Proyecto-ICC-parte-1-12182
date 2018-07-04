#carta
POSTRE = ["Flan","Mazamorra","Pudin","Supiro a la limeña"]
ENTRADA = ["Papa a la huacaína ","Ocopa","Papa rellena","Anticuhos"]
SEGUNDO = ["Aji de Gallina","Chanfainita","Arroz con Pollo","Bistec a lo Pobre"]
BEBIDA = ["Inka Kola","Chicha Morada","Chicha de Jora","Coca Cola"]

hora=input("por último ingrese que hora es (horaminutos):")
if int(hora) < 900:
 print("El restaurante aun no esta abierto, regrese más tarde")
elif int(hora) >= 900:
  print("El restaurante esta abierto, pase por favor")
clientes=int(input("Ingrese el número de clientes el día de hoy:"))
if int(hora)>= 900:
    for x in range (clientes):
        print("[Entorno]: El cliente deja su auto con el valet parking")
        auto_modelo=input("Porfavor, me podría decir el modelo de su auto:")
        placa=input("Y su número de placa:")

print("[Entorno]: El cliente llega al restaurante y se siente.")
print("[Entorno]: El mesero se acerca y le da la bienvenida al restaurante.")
print("[Mesero]: Bienvenidos a Coco's restaurant")
print("[Mesero]: Que se le ofrece.")
print("[Cliente]: Que hay en la carte para empezar.")
print("[Mesero]: De entrada tenemos...")
print(ENTRADA)
