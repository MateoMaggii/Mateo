cadena1 = "Hola soy mateo"
cadena2 = "chaumevoy"
cadena3 = "45839123"

#resultado = cadena1.upper() #hace mayuscula todo
#resultado = cadena1.lower() #minuscula
#resultado = cadena1.capitalize() #primert letra en mayusc

#buscar una cadena en otra cadena, si no hay resultado =-1
#busqueda_find = cadena1.find("s")
#busqueda_index = cadena1.index(1) #si no hay coincidencia lanza error

#si es numerico devuelve true, sino false
#es_numerico = cadena3.isnumeric()
#es_alfanumerico = cadena2.alfanumerico()

#contamos las coincidencias
#contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verifica como empieza una cadena
empieza_con = cadena1.startswith("o")
termina_con = cadena1.endswith("eo")

#remplaza una cadena con la dada
cadena_nueva = cadena1.replace("teo","tea")

#separa cadenas 
cadena_separada = cadena1.split("m")
print(cadena_separada)

