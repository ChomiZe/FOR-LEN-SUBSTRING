#Desarrollar un programa que solicite una frase desde teclado
#el programa debera imprimir en pantalla la frase ingresada sin vocales
#requerimientos
#ciclo o bucle while o for
#considerar vocales mayusculas y minusculas

string = input('Ingrese una frase: ')
letter = input('Con que frase deseas terminar el bucle?: ')

for var1 in string :
    if var1.lower() == letter.lower():
        break
    elif var1.lower() == "a":
        continue
    elif var1.lower() == "e":
        continue
    elif var1.lower() == "i":
        continue
    elif var1.lower() == "o":
        continue
    elif var1.lower() == "u":
        continue
    print(var1, end="")

