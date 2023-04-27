nutricion = open('Dataset.csv', encoding = 'utf-8-sig')

contenido = nutricion.read().splitlines()

#Temporales
masGrasa = 0
nombreGrasa = ""
#
masVitaminaC = 0
nombreVitaminaC = ""
#
contAlimentosTiamina = 0
#
masVitaminas = 0
nombreVitaminas = ""
#
alimentos = []
#

for line in contenido:
    grasas = float(line.strip().split(";")[3].replace(",",".").replace("-","0"))
    hierro = float(line.strip().split(";")[5].replace(",",".").replace("-","0"))
    vitaminaA = float(line.strip().split(";")[6].replace(",",".").replace("-","0"))
    vitaminaB1 = float(line.strip().split(";")[7].replace(",",".").replace("-","0"))
    vitaminaB2 = float(line.strip().split(";")[8].replace(",",".").replace("-","0"))
    vitaminaB3 = float(line.strip().split(";")[9].replace(",",".").replace("-","0"))
    vitaminaC = float(line.strip().split(";")[10].replace(",",".").replace("-","0"))
    
    vitaminas = (vitaminaA * 0.0003) + vitaminaB1 + vitaminaB2 + vitaminaB3 + vitaminaC

    #Alimento con mas grasas
    if (grasas > masGrasa): 
        masGrasa = grasas
        nombreGrasa = line.strip().split(";")[0]
    #Alimento con mas vitamina C
    if (vitaminaC > masVitaminaC): 
        masVitaminaC = vitaminaC
        nombreVitaminaC = line.strip().split(";")[0]
    #Cantidad de alimentos con mas de 0.1g de Vitamina B1 (Tiamina)
    if (vitaminaB1/1000 > 0.1):
        contAlimentosTiamina += 1
    #Alimento con mayor suma de Vitaminas
    if (vitaminas > masVitaminas):
        masVitaminas = vitaminas
        nombreVitaminas = line.strip().split(";")[0]
    #Alimentos con mas de 1mg de hierro y menos de 3g de grasa
    if (hierro > 1 and grasas < 3):
        alimentos.append(line.strip().split(";")[0])
    #

print("\nAlimento con mas grasa:", nombreGrasa, "con", masGrasa,"g")
print("Alimento con mas vitamina C:", nombreVitaminaC, "con", masVitaminaC,"mg")
print("Alimentos con mas de 0.1g Tiamina:", contAlimentosTiamina,"Alimentos")
print("Alimento con mas vitaminas:", nombreVitaminas, "con", masVitaminas,"mg")
print("Alimentos con mas de 1mg de hierro y menos de 3g de grasas:\n",
      alimentos)
""" for i in range(len(alimentos)):
    print(alimentos[i]) """
print("\n")

#

salida = open("Mapper1Result.txt","w", encoding = 'utf-8-sig')

salida.write( str(nombreGrasa) + "\n" + str(masGrasa) + "\n" 
 + str(nombreVitaminaC) + "\n" + str(masVitaminaC) + "\n" 
 + str(contAlimentosTiamina) + "\n" + str(nombreVitaminas) + "\n" 
 + str(masVitaminas) + "\n" + str(alimentos) )

salida.close()