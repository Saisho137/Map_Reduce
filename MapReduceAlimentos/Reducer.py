archivo1 = open("Mapper1Result.txt", encoding = 'utf-8-sig').read().splitlines()
archivo2 = open("Mapper2Result.txt", encoding = 'utf-8-sig').read().splitlines()

#Mayor Grasa
if( float(archivo1[1]) > float(archivo2[1]) ):
    mayorGrasas = float(archivo1[1])
    nombreGrasas = archivo1[0]
else:
    mayorGrasas = float(archivo2[1])
    nombreGrasas = archivo2[0]
print("\nAlimento con mas grasa:", nombreGrasas, "con", mayorGrasas,"g")

#Mayor Vitamina C
if( float(archivo1[3]) > float(archivo2[3]) ):
    mayorVitaminaC = float(archivo1[3])
    nombreVitaminaC = archivo1[2]
else:
    mayorVitaminaC = float(archivo2[3])
    nombreVitaminaC = archivo2[2]
print("Alimento con mas vitamina C:", nombreVitaminaC, "con", mayorVitaminaC,"mg")

#Alimentos > 0.1g Tiamina
alimentosTiamina = float(archivo1[4]) + float(archivo2[4])
print("Alimentos con mas de 0.1g Tiamina:", alimentosTiamina,"Alimentos")

#Mas vitaminas
if( float(archivo1[6]) > float(archivo2[6]) ):
    mayorVitaminico = float(archivo1[6])
    nombreVitaminico = archivo1[5]
else:
    mayorVitaminico = float(archivo2[6])
    nombreVitaminico = archivo2[5]
print("Alimento con mas vitaminas:", nombreVitaminico, "con", mayorVitaminico,"mg")

#Lista de Alimentos
listaAlimentos = []
listaAlimentos.extend(eval(archivo1[7]))
listaAlimentos.extend(eval(archivo2[7]))
print("Lista de Alimentos > 1mg Hierro && < 3g Grasas:", listaAlimentos)
print("\n")

#

salida = open("ReducerResult.txt","w", encoding = 'utf-8-sig')

salida.write( "\nAlimento con mas grasa: " + str(nombreGrasas) + " con " + str(mayorGrasas) + "g" + "\n"
 + "Alimento con mas vitamina C: " + str(nombreVitaminaC) + " con " + str(mayorVitaminaC) + "mg" + "\n"
 + "Alimentos con mas de 0.1g Tiamina: " + str(alimentosTiamina) + " Alimentos." + "\n"
 + "Alimento con mas vitaminas: " + str(nombreVitaminico) + "con" + str(mayorVitaminico) + "mg" + "\n"
 + "Lista de Alimentos > 1mg Hierro && < 3g Grasas: \n" + str(listaAlimentos))

salida.close()