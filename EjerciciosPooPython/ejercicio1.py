import random

class Persona(object):
    def __init__(self, peso = 0, altura = 0,  nombre = "", edad = 0 , sexo = "M"):
        self.__dni = self.generaDNI()
        self.__edad = edad
        self.__nombre = nombre
        self.__sexo = self.introducirSexo(sexo)
        self.__peso = peso
        self.__altura = altura

    def calcularIMC(self):
        IMC = self.__peso/pow(self.__altura, 2)
        if (IMC < 18.5):
            return -1, IMC
        elif (IMC >= 18.5 and IMC <= 24.8):
            return 0, IMC
        return 1, IMC

    def esMayorDeEdad(self):
        if(self.__edad >= 18):
            return True
        return False

    def introducirSexo(self, sexo):
        if(sexo == "H"):
            return "H"
        else:
            return "M"

    def generaDNI(self):
        numeros = ""
        for i in range(8):
            numeros = numeros + str(random.randrange(0, 9, 1))
        letras = "TRWAGMYFPDXBNJZSQVHLCKEO"
        return numeros + letras[int(numeros)%23]

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad

    def setPeso(self, peso):
        self.__peso = peso

    def setSexo(self, sexo = "M"):
        if(sexo == "H"):
            self.__sexo ="H"
        else:
            self.__sexo = "M"

    def setAltura(self, altura):
        self.__altura = altura

    def getDNI(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getPeso(self):
        return self.__peso

    def getSexo(self):
        return self.__sexo

    def getAltura(self):
        return  self.__altura

    """Metodo para mostrar los datos de cada persona"""

    def toString(self):
        print("Nombre: " + self.__nombre)
        print("DNI: " + self.__dni)
        print("Edad: " + str(self.__edad))
        print("Sexo: " + self.__sexo)
        print("Peso: " + str(self.__peso))
        print("Altura: " + str(self.__altura))


"""Devolver si es mayor de edad o no"""
def mayorDeEdad(edad):
    if (edad):
        print("Es mayor de edad")
    else:
        print("Es menor de edad")



if __name__ == "__main__":

    """Ejercicio 1"""

    """Obligar a introducir dato"""

    nombre = input("Introduzca nombre: ")
    while nombre == "":
        nombre = input("Introduzca nombre: ")
    edad = input("Introduzca edad: ")
    while edad == "":
        edad = input("Introduzca edad: ")
    edad = int(edad)
    sexo = input("Introduzca sexo (M/H): ")
    peso = input("Introduzca peso (kg): ")
    while peso == "":
        peso = input("Introduzca peso (kg): ")
    peso = float(peso)
    altura = input("Introduzca altura (m): ")
    while altura == "":
        altura = input("Introduzca altura (m): ")
    altura = float(altura)

    persona1 = Persona(peso, altura, nombre, edad, sexo)

    print("Persona 1")
    print("--------------")
    valor, resultado = persona1.calcularIMC()
    if valor == -1:
        print("Su peso es inferior a lo normal. IMC: " + str(resultado))
    elif valor == 0:
        print("Su peso es normal. IMC: " + str(resultado))
    else:
        print("Su peso es superior a lo normal. IMC: " + str(resultado))

    mayorDeEdad(persona1.esMayorDeEdad())

    print("PERSONA 2")
    print("--------------")
    peso = input("Introduzca peso (kg): ")
    while peso == "":
        peso = input("Introduzca peso (kg): ")
    peso = float(peso)
    altura = input("Introduzca altura (m): ")
    while altura == "":
        altura = input("Introduzca altura (m): ")
    altura = float(altura)
    persona2 = Persona(peso,altura, nombre, edad, sexo)
    valor, resultado = persona2.calcularIMC()
    if valor == -1:
        print("Su peso es inferior a lo normal. IMC: " + str(resultado))
    elif valor == 0:
        print("Su peso es normal. IMC: " + str(resultado))
    else:
        print("Su peso es superior a lo normal. IMC: " + str(resultado))
    mayorDeEdad(persona2.esMayorDeEdad())
    print("PERSONA 3")
    print("--------------")
    persona3 = Persona()
    persona3.setPeso(75)
    persona3.setAltura(1.8)
    valor, resultado = persona3.calcularIMC()
    if valor == -1:
        print("Su peso es inferior a lo normal. IMC: " + str(resultado))
    elif valor == 0:
        print("Su peso es normal. IMC: " + str(resultado))
    else:
        print("Su peso es superior a lo normal. IMC: " + str(resultado))
    mayorDeEdad(persona3.esMayorDeEdad())

    print("DATOS")
    print("--------------")

    print("Persona1")
    print("--------------")
    persona1.toString()
    print("Persona 2")
    print("--------------")
    persona2.toString()
    print("Persona 3")
    print("--------------")
    persona3.toString()