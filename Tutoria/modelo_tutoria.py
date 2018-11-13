class Ciudad(object):
    def __init__(self):
        self.nombrec = " "
        self.poblacion = 0

    def agregarNombreCiudad(self, nc):
        self.nombrec = nc

    def obtenerNombreCiudad(self):
        return self.nombrec

    def agregarPoblacion(self, po):
        self.poblacion = po

    def obtenerPoblacion(self):
        return self.poblacion

class Persona(object):
    def __init__(self):
        self.nombre = " "
        self.apellido = " "
        self.ciudad = Ciudad()

    def agregarNombreEstudiante(self, ne):
        self.nombre = ne

    def obtnerNombreEstudiante(self):
        return self.nombre

    def agregarApellido(self,ap):
        self.apellido = ap

    def obtenerApellido(self):
        return self.apellido

    def agregarCiudad(self, ci):
        self.ciudad = ci

    def obtenerCiudad(self):
        return self.ciudad

    def presentar_Datos(self):
        cadena= "Nombre %s \n Apellido %s  \n Ciudad %s \n Poblacion%s"% (self.obtnerNombreEstudiante(), self.obtenerApellido(), self.obtenerCiudad().obtenerNombreCiudad(), self.obtenerCiudad().obtenerPoblacion())
        return cadena

class Estudiante(Persona):
    def __init__(self):
        super(Estudiante, self).__init__()
        self.estudianted = " "

    def agregarIdEstudiante(self, i):
        self.estudianted = i

    def obtenerIdEstudiante(self):
        return self.estudianted
    def presentar_Datos2(self):
        cadena = "\n ID %s "%(self.obtenerIdEstudiante())
        return cadena

class Est_Presencial(Estudiante):
    def __init__(self):
        super(Est_Presencial, self).__init__()
        self.ciclo = 0
        self.numcre = 0

    def agregarCiclo(self, cic):
        self.ciclo = cic

    def obtenerCiclo(self):
        return self.ciclo

    def agregarNumeroCreditos(self, numc):
        self.numcre = numc

    def obtenerNumeroCreditos(self):
        return self.numcre

    def presentar_Datos3(self):
        cadena = "\nCiclo %s \nNumero de Creditos%s "%(self.obtenerCiclo(), self.obtenerNumeroCreditos())
        return cadena

class Est_Distancia(Estudiante):
    def __init__(self):
        super(Est_Distancia, self).__init__()
        self.modulo = 0
        self.numeroMaterias = 0

    def agregarModulo(self, m):
        self.modulo = m

    def obtenerModulo(self):
        return self.modulo

    def agregarNumeroMaterias(self, nm):
        self.numeroMaterias = nm

    def obtenerNumeroMaterias(self):
        return self.numeroMaterias

    def presentar_Datos4(self):
        cadena = "\nModulo %s \nNumero de Materias %s"%(self.obtenerModulo(), self.obtenerNumeroMaterias())
        return cadena
