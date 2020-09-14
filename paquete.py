class Paquete:
    def __init__(self, id, origen, destino, peso):
        self.__id = id
        self.__origen = origen
        self.__destino = destino
        self.__peso = peso

    def imprimir(self):
        print("Id: ", self.__id)
        print("Origen: ", self.__origen)
        print("Destino: ", self.__destino)
        print("Peso: ", self.__peso)