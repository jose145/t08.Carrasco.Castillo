cad="Sólo conozco dos tipos de personas razonables: las que aman \n a Dios de todo corazón porque le conocen, y las que le buscan de todo corazón porque no le conocen"
#ejercicio 01
print(cad.upper())
print("#"*40)
#ejercicio 02
print(cad.count("las"))

print("#"*40)

#ejercicio 03
print(cad.title())
print("#"*40)

#ejercicio 04
print(cad.replace("las", "david"))

print("#"*40)

#ejercicio 05
print(cad.startswith("S"))


print("#"*40)

cad="    David Carrasco    "
#ejercicio 05
print(cad.strip())
print("#"*40)
#ejercicio 06
print(cad.rstrip())
print("#"*40)
#ejercicio 07
print(cad.lstrip())
print("#"*40)

cad="25"
#ejercicio 08
print(cad.isdigit())
print("#"*40)

cad="Me fui a mi casa a ver la seria, luego fui al mercado, despues me fui a la feria"
#ejercicio 09
print(cad.count("fui"))
print("#"*40)

#ejercicio 10
print(cad.replace("fui", "fue"))
print("#"*40)


#ejercicio 11
print(cad.upper())
print("#"*40)

cad="HOLA COMO ESTA, COMO TE A IDO"
#ejercicio 12
print(cad.lower())
print("#"*40)

#ejercicio 13
print(cad.startswith("COMO"))
print("#"*40)

#ejercicio 14
print(cad.isdigit())
print("#"*40)

cad="Hola,¿Como Estas?,Bien,¿Que haces?"
#ejercicio 15
var=cad.split(",")
for i in var:
    if(i == "Hola"):
        print(i,":Hola")
    if(i == "¿Como Estas?"):
        print(i,":Bien,¿y tu?")
    if(i == "Bien"):
        print(i,":Que bien")
    if(i == "¿Que haces?"):
        print(i,":Nada")


