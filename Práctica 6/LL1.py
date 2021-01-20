'''Instituto Politécnico Nacional
Escuela Superior de Cómputo
Compiladores 3CV6 - Práctica 5
Elaboró - Flores Alvarado Diego Armando
'''
import re

class LL1():

    def __init__(self):
        self.producciones = []
        self.archivo = ''

    @staticmethod
    def obtenerProducciones(archivo):                              #Función para obtener las producciones del archivo.
        f = open (archivo, 'r')
        producciones = []

        for line in f:
            formato = line.rstrip('\n').replace("->", ",").split(",")       #Formato de las producciones en arreglos.
            producciones.append(formato)                                    #Se guardan las producciones en una colección.

        f.close()                                                           #Se cierra el archivo.
        return producciones

class Auxiliares():
    @staticmethod
    def primeros(producciones):
        primeros = []                                                       #Colección que contendrá los primeros de las producciones.
        prim = []                                                           #Colección auxiliar.

        for i in producciones:                                              #Ciclo que recorre cada una de las producciones.
            prod = i[1]                                                     #Toma los datos de la producción.
            a = re.findall("[a-z]", prod[0])                                #Compara si es un símbolo terminal, no terminal o épsilon.
            b = re.findall("(^[ABCDFGHIJKLMNOPQRSTUVWXYZ])", prod[0])
            c = re.findall("(^E)", prod[0])
            
            if (a):                                                         #Si es un símbolo terminal...
                prim.append(prod[0])                                        #Se toma el valor que tenga la producción y se guarda dentro de una colección.
                primeros.append(prim)                                       #Se guarda el valor del primero dentro de la colección de primeros.
                prim = []                                                   #Se limpia la colección auxiliar.

            elif (b):                                                       #Si es un símbolo NO terminal...
                for h in producciones:                                      #Se vuelven a recorrer las producciones para encontrar las producciones que dependan del símbolo no terminal.
                    if (h[0] == prod[0]):                                   #Si la producción depende del símbolo no terminal...
                        pro = h[1]                                          #Se toma el valor que tenga la producción.

                        ab = re.findall("[a-z]", pro[0])                    #Se verifica si es un símbolo terminal, no terminal o épsilon.
                        bb = re.findall("(^[ABCDFGHIJKLMNOPQRSTUVWXYZ])", pro[0])
                        cb = re.findall("(^E)", prod[0])

                        if (ab):                                            #Si es un símbolo terminal...
                            prim.append(pro[0])                             #Se toma el valor que tenga la producción y se guarda dentro de una colección.

                        elif (bb):                                          #Si es un símbolo NO terminal...
                            Auxiliares.primeros(prod)                       #Se vuelven a recorrer las producciones para encontrar las producciones que dependan del símbolo no terminal.

                        elif (cb):
                            prim.append(pro[0])
                rep = dict.fromkeys(prim)                                   #Se eliminan los valores repetidos.
                prim = []                                                   #Se limpia la colección auxiliar.
                for l in rep:                                               #Se ingresan los valores primeros dentro de una colección.
                    prim.append(l)                                          
                primeros.append(prim)                                       #Se agrega la colección de primeros de un símbolo no terminal a la colección de primeros de todas las producciones.
                prim = []                                                   #Se limpia la colección auxiliar.

            elif (c):
                prim.append(prod[0])                                        #Se toma el valor que tenga la producción y se guarda dentro de una colección.
                primeros.append(prim)                                       #Se guarda el valor del primero dentro de la colección de primeros.
                prim = []                                                   #Se limpia la colección auxiliar.

        return primeros
                        
    @staticmethod
    def siguientes(producciones):
        siguientes = []
        sig = []
        terminal = []                                                       #Se guardarán los símbolos no terminales.

        for m in producciones:                                              #Recorre todas las producciones.
            terminal.append(m[0])                                           #Guarda los símbolos No terminales en una colección.
        rep = dict.fromkeys(terminal)                                       #Se eliminan los símbolos repetidos.
        terminal = []                                                       #Se limpia la colección.
        for l in rep:                                                       
            terminal.append(l)                                              #Se reinsertan los elementos sin repeticiones en la colección.
        rep = []                                                            #Se limpia la colección auxiliar.

        for n in terminal:                                                  #Recorre cada uno de los símbolos no terminales.
            for o in producciones:                                          #Recorre cada una de las producciones.
                ra = re.findall(n, o[1])                                    #Comprueba si el símbolo no terminal se encuentra en la producción actual.
                if (ra):                                                    #Si existe...
                    if ((o[1].split(n,1)[0]) and (o[1].split(n,1)[1])):     #Realiza la verificación del formato de la Regla 3 de Siguiente().
                        rb = re.findall("(^E)", o[1])

                        if (rb):
                            print("Regla 4")
                        else:
                            #primero = Auxiliares.primeros()
                            sig.append(primero)
                    elif (o[1].split(n,1)[0]):                              #Realiza la verificación del formato de la Regla 2 de Siguiente().    
                        print("Regla 2")
                    else:                                                   #Si el formato no concuerda con alguna de las reglas, se regresa error.
                        print("El formato de tu producción no coincide con ninguna de las reglas, favor de validar.")
                        break


            #if (m == producciones[0]):
            #    sig.append("$")

    @staticmethod
    def siguiente(produccion):
        print("solo una")
            
            

archivo = 'prueba.txt'
xd = LL1.obtenerProducciones(archivo)
pd = Auxiliares.primeros(xd)
#pd = Auxiliares.siguientes(xd)
print(pd)