import sys
#import tkFileDialog 
#import tkMessageBox
#from ScrolledText import *
#import ttk

import decimal
import random
import math
import copy
decimal.getcontext().prec = 3
class FuncionNormalizar:	
	def normalizacion(self, vector):
		self.DesEstandar=float(0)
		self.Media=float(0)
		prom=float(0)
		self.DE=float(0)
		self.vectorNormalizado = []
		for i in range(len(vector)):
			prom=prom+float(vector[i])

		self.media=round(decimal.Decimal(prom/(len(vector))),3)
		#print "media", self.media
		self.vectorNormalizado.append(self.media)
		self.desv=0
		for i in range(len(vector)):
			self.desv=float(pow((float(vector[i])-self.media),2))+self.desv
		#print "desv es", self.desv
		#modificado
		self.DE=round(decimal.Decimal(math.sqrt(decimal.Decimal(self.desv)/(len(vector)-1))),3)
		#print "desviacion estandar", self.DE
		self.vectorNormalizado.append(self.DE)
		#self.vectorNormalizado = []
		for e in vector:
			try:
				norma1=self.sigmoide(float((float(e)-self.media)/self.DE))
			except ZeroDivisionError:
				norma1=0
			self.vectorNormalizado.append(norma1)
		self.Media=self.media
		self.DesEstandar=self.DE
		#print self.vectorNormalizado
		return self.vectorNormalizado
	def sigmoide(self, net):
		exp=decimal.Decimal(2.718281)
		self.resultado=(decimal.Decimal(1)/(1+pow(decimal.Decimal(exp),decimal.Decimal(-net))))
		return self.resultado

	def main(self, datos):

		resultados=self.normalizacion(datos)
		return resultados