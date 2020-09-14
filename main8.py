from paqueteria import Paqueteria
from paquete import Paquete

p = Paqueteria()

while True:
    print('1) Agregar')
    print('2) Mostrar')
    print('0) Salir')
    op = input()

    if op == "1":
        id = input("Id: ")
        origen = input("Origen: ")
        destino = input("Destino: ")
        peso = float(input("Peso: "))

        paquete = Paquete(id, origen, destino, peso)

        p.agregar(paquete)
    elif op == "2":
        p.mostrar()
    elif op == "0":
        break

