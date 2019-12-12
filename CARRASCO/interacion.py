#ejercicio 01
cad="Claro que no, porque tendria odio a alguien que es mas debil que yo. \n by:\"Escanor\""
vocal_a=0
vocal_e=0
vocal_i=0
vocal_o=0
vocal_u=0

for vocal in cad.lower():
    if(vocal=="a"):
        vocal_a +=1
    if(vocal=="e"):
        vocal_e +=1
    if(vocal=="i"):
        vocal_i +=1
    if(vocal=="o"):
        vocal_o +=1
    if(vocal=="u"):
        vocal_u +=1
print(cad)
print("La cantida de vocales \"a\" es:", vocal_a)
print("La cantida de vocales \"e\" es:", vocal_e)
print("La cantida de vocales \"i\" es:", vocal_i)
print("La cantida de vocales \"o\" es:", vocal_o)
print("La cantida de vocales \"u\" es:", vocal_u)

print("#"*40)
#ejercicio 02
for nombre in range(10):
    nombre="David"
    print(nombre)

print("#"*40)

#ejercicio 03
#contraseña debe tener un numero

contraseña="DavidCarrasco2"
for val in contraseña:
    if(val.isdigit()==True):
        print("Contraseña es correcta")

print("#"*40)


#ejercicio 04
msg="ABCDE"
for letra in msg:
    if letra=="A":
        print("Hola como estas")
    if letra=="B":
        print("Ella no te quiere")
    if letra=="C":
        print("Compra pan")
    if letra=="E":
        print("¿Mañana hay tarea?")


print("#"*40)

#ejercicio 05
cad="DCV"
for letra in cad:
    if(letra=="D"):
        print(letra+"avid")
    if(letra=="C"):
        print(letra+"arrasco")
    if(letra=="V"):
        print(letra+"idaurre ")



print("#"*40)


#ejercicio 06
#verificador de email
email="dcarrascov@gmail.com"
msg="El gmail es {gmail}"
verificador=False


for i in email:
    if(i=="@"):
        verificador=True

    #fin bucle

if(verificador==True):
    print("gmail es correcto")

else:
    print("gmail incorrecto")
print(msg.format(gmail=email))

print("#"*40)

#ejercicio 07
cad="Pedro ruiz gallo\n"
for letras in cad.upper():
    print(letras, end=" ")


print("#"*40)

#ejercicio 08
cad="Facultad de Ciencias Fisica y Matematicas\n"
for i in cad.title():
    print(i, end=" ")
print("#"*40)


#ejercicio 09
cad="ABCDE24"
for letra in cad:
    if(letra=="A"):
        print(letra+": Hola")
    if(letra=="B"):
        print(letra+": Que tal")
    if(letra=="C"):
        print(letra+": Ya me voy")
    if(letra=="D"):
        print(letra+": Ell no te ama")
    if(letra=="E"):
        print(letra+": Feliz navidad")
    if(letra=="2"):
        print(letra+": 14 dias para navidad ")
    if(letra=="4"):
        print(letra+": 19 dias para fin de año")

print("#"*40)
#ejercicio 10
cad="PVOI"

for letra in cad:
    if(letra=="P"):
        print(letra+": Primavera")
    if(letra=="V"):
        print(letra+": Verano")
    if(letra=="O"):
        print(letra+": Otoño")
    if(letra=="I"):
        print(letra+": Invierno")
print("#"*40)

#ejercicio 11
pos=1
cad="Feliz Navidad"
msg=cad.split(" ")
for i in msg:
    if(pos==1):
        print(i.center(30))
    if(pos==2):
        print(i.center(30))
    pos+=1

print("#"*40)

#ejericio 12
cad="ingenieria electronica\n"
for letra in cad.upper():
    print(letra, end=" ")

print("#"*40)

#ejercicio 13
cad="########"
espacio=" "
pos=1

for rama in cad.upper():
    if(pos==1):
        print(espacio*16+rama)
    if(pos==2):
        print(espacio*15+rama*3)
    if(pos==3):
        print(espacio*14+rama*5)
    if(pos==4):
        print(espacio*13+rama*7)
    if(pos==5):
        print(espacio*12+rama*9)
    if(pos==6):
        print(espacio*11+rama*11)
    if(pos==7):
        print(espacio*10+rama*13)
    if(pos==8):
        print(espacio*9+rama*15)
    pos+=1
#fin_for

print(" "*16+"○")
print(" "*16+"○")
print("x"*40)
#ejercicio 14
cad="Universidad Nacional Pedro Ruiz Gallo\n"
for letra in cad.title():
    print(letra, end=" ")
print("x"*40)



#ejercicio 15
cad="Fernando Diaz Sanchez"
for letra in cad:
    print(letra.upper().center(30))
