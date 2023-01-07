# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:06:25 2013

@author: miguel
"""

class Simbolo(object):
    
    def __init__(self,dato,p):        
        self.simbolo = dato
        self.probabilidad = p
        self.codigo = ""
        self.sucesor = None
    
    def getProbabilidad(self):
        return self.probabilidad
    
    def getSucesor(self):
        return self.sucesor

    def getSimbolo(self):
        return self.simbolo
    
    def setSucesor(self,nuevo):
        self.sucesor = nuevo
    
    def setCodigo(self,c):
        self.codigo += c
    
    def getCodigo(self):
        return self.codigo