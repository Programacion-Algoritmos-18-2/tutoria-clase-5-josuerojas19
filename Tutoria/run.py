from modelo_tutoria import *
c1 = Ciudad()
c1.agregarNombreCiudad("Loja")
c1.agregarPoblacion(464646)
e1 = Est_Presencial()
e1.agregarNombreEstudiante("Pedro")
e1.agregarApellido("Torres")
e1.agregarCiudad(c1)
e1.agregarIdEstudiante("1255662")
e1.agregarCiclo(5)
e1.agregarNumeroCreditos(56)
print(e1.presentar_Datos(), e1.presentar_Datos2(), e1.presentar_Datos3())