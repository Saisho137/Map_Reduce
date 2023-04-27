archivo1 = open("resultadoMapper1.txt", encoding = "utf-8").read().splitlines()
archivo2 = open("resultadoMapper2.txt", encoding = "utf-8").read().splitlines()

mejorNota = 0
peorNota = 0

if( int(archivo1[0]) > int(archivo2[0]) ):
    mejorNota += int(archivo1[0])
else:
    mejorNota += int(archivo2[0])

if( int(archivo1[1]) > int(archivo2[1]) ):
    peorNota += int(archivo1[1])
else:
    peorNota += int(archivo2[1])

encimaPromedio = int(archivo1[2]) + int(archivo2[2])
contEstrato = int(archivo1[3]) + int(archivo2[3])

print("\nPuntaje más alto: " + str(mejorNota) + "\nPuntaje más alto: " + str(peorNota))
print("La cantidad de Estudiantes con un promedio encima de 60 es: " + str(encimaPromedio))
print("La cantidad de Estudiantes con un Estrato de 5 o 6: " + str(contEstrato))

salida = open("resultadoFinalReducer.txt","w")
salida.write("Puntaje más alto: " + str(mejorNota) + "\nPuntaje más alto: " + str(peorNota) 
             + "\nLa cantidad de Estudiantes con un promedio encima de 60 es: " + str(encimaPromedio) 
             +"\nLa cantidad de Estudiantes con un Estrato de 5 o 6: " + str(contEstrato))
salida.close()