"""Superclase Electrodomerstico"""
COLOR = "blanco"
PRECIOBASE = 100
CONSUMOENERGETICO = "F"
PESO = 5
class Electrodomestico:

    def __init__(self, precioBase = PRECIOBASE, color = COLOR, consumoEnergetico = CONSUMOENERGETICO, peso = PESO):
        self.__precioBase = precioBase
        self.__color = self.comprobarColor(color)
        self.__consumoEnergetico = self.comprobarConsumoEnergetico(consumoEnergetico)
        self.__peso = peso

    def getPrecioBase(self):
        return self.__precioBase

    def getColor(self):
        return self.__color

    def getConsumoEnergetico(self):
        return self.__consumoEnergetico

    def getPeso(self):
        return self.__peso

    def comprobarConsumoEnergetico(self, letra):
        if(letra == "A"):
            return "A"
        elif(letra == "B"):
            return "B"
        elif(letra == "C"):
            return "C"
        elif(letra == "D"):
            return "D"
        elif(letra == "E"):
            return "E"
        return "F"

    def comprobarColor(self, color):
        if(color == "negro"):
            return "negro"
        elif(color == "rojo"):
            return "rojo"
        elif(color == "azul"):
            return "azul"
        elif(color == "gris"):
            return "gris"
        return "blanco"

    def precioFinal(self):
        precioFinal = 0
        if(self.__consumoEnergetico == "A"):
            precioFinal = self.__precioBase + 100
        elif (self.__consumoEnergetico == "B"):
            precioFinal = self.__precioBase + 80
        elif (self.__consumoEnergetico == "C"):
            precioFinal = self.__precioBase + 60
        elif(self.__consumoEnergetico == "D"):
            precioFinal = self.__precioBase + 50
        elif(self.__consumoEnergetico == "E"):
            precioFinal = self.__precioBase + 30
        elif (self.__consumoEnergetico == "F"):
            precioFinal = self.__precioBase + 10

        if(self.__peso >= 0 and self.__peso<=19):
            precioFinal += 10
        elif(self.__peso >= 20 and self.__peso<=49):
            precioFinal += 50
        elif(self.__peso >= 50 and self.__peso<=79):
            precioFinal += 80
        else:
            precioFinal += 100
        return precioFinal

"""Subclase lavadora"""
class Lavadora(Electrodomestico):
    CARGA = 5

    def __init__(self, precioBase = PRECIOBASE, color = COLOR, consumoEnergetico =CONSUMOENERGETICO , peso = PESO, carga = CARGA):
        super().__init__(precioBase, color, consumoEnergetico, peso)
        self.__carga = carga

    def getCarga(self):
        self.__carga

    def precioFinal(self):
        precioFinal = super(Lavadora, self).precioFinal()
        if(self.__carga > 30):
            precioFinal += 50
        return precioFinal

"""Subclase Television"""
class Television(Electrodomestico):
    def __init__(self, precioBase=PRECIOBASE, color=COLOR, consumoEnergetico=CONSUMOENERGETICO, peso=PESO, pulgadas = 20, fourK = False):
        super().__init__(precioBase, color, consumoEnergetico, peso)
        self.__pulgadas = pulgadas
        self.__fourK = fourK

    def getPulgadas(self):
        return self.__pulgadas

    def getFourK(self):
        return self.__fourK

    def precioFinal(self):
        precioFinal = super(Television, self).precioFinal()
        if(self.__pulgadas > 40):
            precioFinal *= 1.30
        if(self.__fourK):
            precioFinal += 50
        return precioFinal


"""Clase ejecutable"""
class ejecutable:

    def __init__(self):
        self.__lista = self.crearLista()

    def crearLista(self):
        lista = []
        lista.append(Lavadora())
        lista.append(Television())
        lista.append(Television(pulgadas = 32, fourK = True))
        lista.append(Television(300, "gris", "B", 10, 32, True))
        lista.append(Lavadora(carga = 10))
        lista.append(Lavadora(250, "blanco", "D", 50, 8))
        lista.append(Lavadora(250, "blanco", "B", 60, 8))
        lista.append(Television(300, "gris", "B", 10, 32, True))
        lista.append(Lavadora(300, "blanco", "D", 50, 7))
        lista.append(Television(200, "rojo", "C", 10, 42, False))
        return lista

    def precioFinal(self):
        precioFinal = 0
        precioLavadoras = 0
        precioTelevisiones = 0

        for i in self.__lista:
            print(i.precioFinal())
            precioFinal += i.precioFinal()
            if type(i) == Lavadora:
                precioLavadoras += i.precioFinal()
            elif type(i) == Television:
                precioTelevisiones += i.precioFinal()


        return precioFinal,precioLavadoras, precioTelevisiones

if __name__ == "__main__":
    ejecutable = ejecutable()
    print("Precio final: %d €, lavadoras; %d €, televisiones: %d €" %(ejecutable.precioFinal()))