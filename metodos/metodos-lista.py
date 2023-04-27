lista = list(["hola","como estas"])

cantidad_de_elementos = len(lista)

lista.append("jajajaajaj") #agrega algo a la lista

lista.insert(2,"toma mama") #intercambia algo de la lista por lo que le pones

lista.extend([False,2020]) 

print(len(lista))

lista.pop(0) #ELIMINA UN ELEMENTO

print(len(lista))

#remueve un elemento de la lista por su valor
lista.remove("toma mama")
#lista.clear()
#lista.short() #ordena la lista
#lista.reverse()

print(lista)