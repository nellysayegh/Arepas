#Solicitud de ingredientes para arepas 
harina_pan = float(input("Escriba la cantidad de harina pan en tazas: ")) 
agua = float(input("Escriba la cantidad de agua en tazas: "))
sal = float(input("Escriba la cantidad de sal en cucharaditas: "))
aceite = float(input("Escriba la cantidad de aceite en cucharadas: "))

#Conversion de cucharaditas de sal a tazas
tazas_sal = (sal / 3) / 16

#Conversion de cucharadas de aceite a tazas 
tazas_aceite = aceite / 16

#Calculo de cantidad de masa 
masa = (harina_pan + agua + tazas_sal + tazas_aceite)
print("La cantidad de tazas de masa es: " + str(masa))

#Calculo de cantidad de arepas cada una de 1/2 taza
cantidad_arepas = int(masa / 1/2)
print("Con esas tazas de masa puedes hacer: " +str(cantidad_arepas) +' arepas de 1/2 taza cada una')