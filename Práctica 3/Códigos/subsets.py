'''Instituto Politécnico Nacional
Escuela Superior de Cómputo
Compiladores 3CV6 - Práctica 3
Elaboró - Flores Alvarado Diego Armando
'''

class subsets():

    def __init__(self):
        self.contenido = ""                                             #Guarda el contenido del archivo.
        self.inicial = []                                               #Estado inicial del AFN
        self.finales = []                                               #Estados finales del AFN.
        self.destados = []                                              #Guarda los Destados.
        self.trancisionesAFN = []                                       #Transiciones del AFN.
        self.alfabeto = []                                              #Alfabeto del AFN.
        self.resCerraduraEpsilon = []                                   #Lista con los estados que obtiene la Cerradura Epsilon.
        self.resMover = []                                              #Lista con los estados que obtiene la operación Mover.

    @staticmethod
    def obtenerInicial(archivo):                                   #Función para obtener el estado inicial.
        f = open (archivo, 'r')
        inicial = []

        for lines in f:
            if 'inicial' in lines:
                ini = lines.split(":")[-1].strip()
                inicial.append(ini)
        
        f.close()
        return inicial

    @staticmethod
    def obtenerFinales(archivo):                                   #Función para obtener los estados finales.
        f = open (archivo, 'r')
        finales = []

        for lines in f:
            if 'finales' in lines:
                fin = lines.split(":")[-1].strip()
                finales = fin.split(",")

        f.close()
        return finales

    @staticmethod
    def obtenerTransiciones(archivo):                              #Función para obtener las transiciones del AFN.
        f = open (archivo, 'r')
        trancisionesAFN = []

        for i in range(2):
            f.readline()
        for line in f:
            formato = line.rstrip('\n').replace("->", ",").split(",")
            trancisionesAFN.append(formato)

        f.close()
        return trancisionesAFN

    @staticmethod
    def obtenerAlfabeto(trancisionesAFN):
        transiciones = trancisionesAFN
        alfa = []
        
        for trans in transiciones:
            if (trans[2] != 'E'):
                if not trans[2] in alfa:
                    alfa.append(trans[2])
        
        alfabeto = sorted(alfa)
        return alfabeto

    @staticmethod
    def cerraduraEpsilon(trancisionesAFN, estado):                                 #Aplica la Cerradura de Epsilon a uno o más estados.
        transiciones = trancisionesAFN
        estados = estado
        resultado = []
        rescerraduraEpsilon = []

        for i in estados:
            for trans in transiciones:
                if trans[0] == i:
                    if trans[2] == 'E':
                        resultado.append(trans[1])
                        estados.append(trans[1])
                        resultado.append(i)

        res = list(dict.fromkeys(estados))      #Lista con los resultados de la cerradura Epsilon (Se eliminan duplicados).
        rescerraduraEpsilon = sorted(res)       #Lista con los resultados de la cerradura Epsilon ordenados de menor a mayor.
        return rescerraduraEpsilon

    @staticmethod
    def mover(trancisionesAFN, T, a):                                                 #Función que aplica la operación Mover.
        transiciones = trancisionesAFN
        resultado = []

        for i in T:
            for trans in transiciones:
                if trans[0] == i:
                    if trans[2] == a:
                        resultado.append(trans[1])

        resMover = sorted(resultado)               #Lista con los resultados de la operación Mover ordenados de menor a mayor.
        return resMover

    def AFNtoAFD(self, archivo):                                    #Función que realiza la conversión de un AFN a un AFD usando el algoritmo de los subconjuntos.
        destados = []                                               #Lista donde se depositarán los Destados.
        destadosMarcados = []                                       #Lista donde se depositarán los DestadosMarcados (Bandera).
        Dtrans = []                                                 #Lista donde se depositarán las Transiciones
        
        AFD = subsets()
        inicial = AFD.obtenerInicial(archivo)                       #Obtiene el estado inicial.
        finales = AFD.obtenerFinales(archivo)                       #Obtiene los estados finales.
        transiciones = AFD.obtenerTransiciones(archivo)             #Obtiene las transiciones.
        alfabeto = AFD.obtenerAlfabeto(transiciones)                #Obtiene el alfabeto del autómata.

        A = AFD.cerraduraEpsilon(transiciones, inicial)             #Realiza la cerradura Epsilon inicial.
        destados.append(A)
        destadosMarcados.append(A)                                  #Guarda el primer destado.

        while(destadosMarcados != []):                              #Algortimo de los subconjuntos.
            des = subsets()                                         

            for destado in destados:                                #Para cada Destado dentro de la lista de Destados
                for a in alfabeto:                                  #Para cada elemento del alfabeto.
                    mov = des.mover(transiciones,destado,a)         #Se aplica la operación Mover, recibe las transiciones del autómata, el destado, y el elemento del alfabeto.
                    U = des.cerraduraEpsilon(transiciones,mov)      #Aplica la Cerradura Epsilon al resultado de la operación Mover
                    for d in destados:                              
                        if U not in destados:                       #Comprueba que el destado resultante se encuentre (o no) en el arreglo de destados.
                            destados.append(U)                      #Agrega el destado a la lista de Destados.
                            destadosMarcados.append(U)              #Agrega el destado a la lista de Destados Marcados.
                    tran = [destado, a, U]                          
                    Dtrans.append(tran)                             #Agrega la transición a la lista de transiciones.
                destadosMarcados.remove(destado)                    #Elimina el DestadoMarcado actual para asi avanzar con el siguiente DestadoMarcado