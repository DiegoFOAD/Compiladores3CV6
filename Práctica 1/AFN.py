import re

class AFN():

    def __init__(self):
        self.contenido = ""
        self.inicial = 0
        self.finales = []
        self.AFD = False
        self.AFN = False

    def cargar_desde(self,archivo):
        f = open (archivo, 'r')
        mensaje = f.read()
        f.close()
        self.contenido = mensaje

        return self.contenido

    def guardar_en(self,archivo,contenido):
        f = open (archivo, 'w')
        f.write(contenido)
        f.close()

    def obtener_inicial(self,archivo):
        f = open (archivo, 'r')
        
        for lines in f:
            if 'inicial' in lines:
                inicial = lines.split(":")[-1].strip()
        
        self.inicial = inicial

    def obtener_finales(self,archivo):
        f = open (archivo, 'r')

        for lines in f:
            if 'finales' in lines:
                separate = lines.split(":")[-1].strip()

        finales = separate.split(',')
        self.finales = finales

    def establecer_inicial(self,estado):
        self.inicial = estado

    def establecer_finales(self,estados):
        self.finales = estados

    def esAFN(self,archivo):
        f = open (archivo, 'r')

        for lines in f:
            if 'E' in lines:
                self.AFN = True
            
            else:
                self.AFN = False

    def esAFD(self,archivo):
        f = open (archivo, 'r')

        for lines in f:
            if 'E' in lines:
                self.AFD = False

            else:    
                self.AFD = True