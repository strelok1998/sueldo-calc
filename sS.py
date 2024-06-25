#!/usr/bin/python3


retencion = float (21.500898563)

print("Calculadora de sueldos con retenciones y aumentos")

#Aumento
print("¿De cuanto fue el porcentaje de aumento de este mes?")
aumento = int(input())


print("\nPor favor ingrese su sueldo mensual en bruto")


sueldo_mensual = float(input())

monto_aumento = (sueldo_mensual * aumento) // 100

print("El monto de aumento en pesos es de \n $",monto_aumento)

monto_total = float(sueldo_mensual + monto_aumento)

print("Sueldo total en bruto con aumento \n $",monto_total)

total_ret = float((monto_total * retencion) // 100)

print("La retencion total es de: \n $", total_ret, "pesos") 

sueldo_neto = float(monto_total - total_ret)

print("Usted va a cobrar este mes la suma de \n $", sueldo_neto , "pesos") 

