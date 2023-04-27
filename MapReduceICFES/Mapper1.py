archivo = open('DatosICFES.csv', encoding = 'utf-8')

contenido = archivo.read().splitlines()

mejorNota = 0
peorNota = 101
encimaPromedio = 0
contEstrato = 0

for linea in contenido:
    lenguaje = int(linea.split(';')[6])
    matematicas = int(linea.split(';')[7])
    ciencias = int(linea.split(';')[8])
    sociales = int(linea.split(';')[9])
    try:
        ingles = int(linea.split(';')[10])
    except:
        ingles = 0
    estrato = linea.split(';')[5]

    #Mejor resultado matematicas
    if (matematicas > mejorNota): mejorNota = matematicas
    #Peor resultado matematicas
    if (matematicas < peorNota): peorNota = matematicas
    #Promedio encima de 60
    temp = (lenguaje + matematicas + ciencias + sociales + ingles)/5
    if (temp>60): encimaPromedio += 1
    #Estrato 5 o 6
    if (estrato == 'Estrato 5' or estrato == 'Estrato 6'): contEstrato += 1

salida = open("resultadoMapper1.txt","w")
salida.write( str(mejorNota) + "\n" + str(peorNota) + "\n" + str(encimaPromedio) + "\n" + str(contEstrato) )
salida.close()