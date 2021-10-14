"""Clase serie"""
class Serie:

    def __init__(self, titulo, genero, creador, numeroTemporadas = 3):
        self.__titulo = titulo
        self.__numeroTemporadas = numeroTemporadas
        self.__entregado = False
        self.genero = genero
        self.__creador = creador

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setNumeroTemporadas(self, numeroTemporadas):
        self.__numeroTemporadas = numeroTemporadas

    def setGenero(self, genero):
        self.genero = genero

    def setCreador(self, creador):
        self.__creador = creador

    def getTitulo(self):
        return self.__titulo

    def getNumeroTemporadas(self):
        return self.__numeroTemporadas

    def getGenero(self):
        return self.genero

    def getCreadpr(self):
        return self.__creador

    def entregar(self):
        self.__entregado = True

    def getEntregado(self):
        return self.__entregado

"""Clase videojuego"""
class Videojuego:

    def __init__(self, titulo, genero, compañia, horasEstimadas = 10):
        self.__titulo = titulo
        self.__horasEstimadas = horasEstimadas
        self.__entregado = False
        self.genero = genero
        self.__compañia = compañia

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setHorasEstimadas(self, horasEstimadas):
        self.__horasEstimadas = horasEstimadas

    def setGenero(self, genero):
        self.genero = genero

    def setCreador(self, creador):
        self.__creador = creador

    def getTitulo(self):
        return self.__titulo

    def getHorasEstimadas(self):
        return self.__horasEstimadas

    def getGenero(self):
        return self.__genero

    def getCompañia(self):
        return self.__compañia

    def entregar(self):
        self.__entregado = True

    def getEntregado(self):
        return self.__entregado

if __name__ == "__main__":
    series = []
    videojuegos = []

    series.append(Serie("Juego de tronos", "Drama", "George R.R,", 8))
    series.append(Serie("Breaking Bad", "Drama", "Vince Gilligan,", 5))
    series.append(Serie("Los soprano", "Drama", "David Chase,", 6))
    series.append(Serie("Chernobyl", "Drama", "Craig Mazin,", 1))
    series.append(Serie("Vikingos", " Aventura, Drama, Histórico", " Michael Hirst", 6))

    videojuegos.append(Videojuego("Red Dead Redemption 2", "Aventura", "Rockstar Studios", 720))
    videojuegos.append(Videojuego("The Last Of Us Parte II", "Aventura", "Naughty Dog", 80))
    videojuegos.append(Videojuego("God of War II", "Aventura", "Santa Monica Studio", 200))
    videojuegos.append(Videojuego("Metal Gear Solid", "Acción", "Konami", 120))
    videojuegos.append(Videojuego("Resident Evil 2", "Terror", "Biohazard 2", 70))

    series.__getitem__(3).entregar()
    series.__getitem__(1).entregar()
    series.__getitem__(4).entregar()
    videojuegos.__getitem__(3).entregar()
    videojuegos.__getitem__(2).entregar()

    """Entregados"""

    videojuegosEntregados = []
    seriesEntregadas = []

    for i in videojuegos:
        if i.getEntregado():
            videojuegosEntregados.append(i)

    print("El número de videojuegos entregados son " + str(len(videojuegosEntregados)) + ":")
    for i in videojuegosEntregados:
        print("- " + i.getTitulo())

    for i in series:
        if i.getEntregado():
            seriesEntregadas.append(i)

    print("El número de series entrgaedas son " + str(len(seriesEntregadas)) + ":")
    for i in seriesEntregadas:
        print("- " + i.getTitulo())

    """Serie y videojuego con más tenporadas o horas"""
    maximoTemporadas = 0
    for i in series:
        if(i.getNumeroTemporadas() > maximoTemporadas):
            maximoTemporadas = i.getNumeroTemporadas()
            serie = i

    maximoHoras = 0
    for i in videojuegos:
        if (i.getHorasEstimadas() > maximoHoras):
            maximoHoras = i.getHorasEstimadas()
            videojuego = i

    print("Serie con más temporadas:")
    print("Nombre: " + serie.getTitulo() + ", temporadas: " + str(serie.getNumeroTemporadas()))
    print("Juego con mas horas:")
    print("Nombre: " + videojuego.getTitulo() + ", horas: " + str(videojuego.getHorasEstimadas()))