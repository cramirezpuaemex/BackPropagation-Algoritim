import sys
from Tkinter import *
import tkFileDialog 
import tkMessageBox
from ScrolledText import *
import ttk
from OpenFile import *
import decimal
import random
import math
from tkFileDialog import askopenfilename
from FuncionNormalizar import *
decimal.getcontext().prec = 3
class NormalizaAproximar():
	filename = ""
	pathArchivoDE=None
	def pathfile(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		tkMessageBox.showinfo("Tipo de archivo", "Selecciona el archivo de datos que tenga las siguientes caracteristicas:\n\n-> El archivo debe tener extencion .txt\n \n->Los atributos son separados por comas\n \n-> El valor esperado es el ultimo atributo, seguido de un salto de linea")

		self.filename = askopenfilename(title="Selecciona el archivo para normalizar Aprox. extencion .txt") # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
	def abrirArchivo(self):

		archivo =self.pathfile()
		#self.etiquetaPath.config(text=archivo)
		self.pathArchivoDE=archivo
		return(self.pathArchivoDE)
		
		
	def trabajar(self, nombre):
		#print  "aqui si llega, nombre", nombre
		data = self.leerArchivo(nombre)
		print "data", len(data[0])
		self.X = [[] for e in range(len(data[0]))]

		#el ultimo vector de X son los valores esperados

		for conjunto in data:
			for i in range(len(conjunto)):
				self.X[i].append(conjunto[i])
		#print  self.X
		self.normalizar()

	def leerArchivo(self, ruta):
		print  "aqui si llega, nombre", ruta
		f = open(ruta,"r")
		self.arreglo= []
		while True:
			linea = f.readline()
			if linea:
				datos = linea.split('\n')
				datos = datos[0].split(',')
				##print  datos
				##print  len(datos) 
				try:
					data = [decimal.Decimal(elemento) for elemento in datos]
					##print  data

					self.arreglo.append(data)
				except Exception, e:
					print  e
			else:
				break
		return self.arreglo

	def GuardarDatos(self):
		############################################################################################################################################################################################################
 
		tkMessageBox.showinfo("Guardar Archivo Clasificar", "-> Seleccionar la carpeta para guardar el archivo estadistico (Aprox.)\n\n-> Ingresar en la caja de texto el nombre del archivo para la MEDIA y DES. ESTANDAR de cada atributo")
		f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt",title="Ingresa el nombre para el archivo:MEDIA y DES. ESTANDAR (Aprox). extencion .txt")
		#f.write("Numero de Clases: " + str(len(self.b))+"\n")
		cont=0
		vecAux=[]
		print "len de self.x", len(self.X[0])
		print "len de x1", len(self.X)
		cont0=0
		cont1=0
		rep=0
		for u in range(2):
			Aux=[]
			for i in range(len(self.X)):
				Aux.append(self.X[i][0])
				del self.X[i][0]
			print "aaux", Aux
			vecAux.append(Aux)
		for i in vecAux:
			for j in i:
				f.write(str(j)+",")
			f.write("\n")
		f.close() # `()` was missing
		############################################################################################################################################################################################################
		tkMessageBox.showinfo("Guardar Archivo", "-> Seleccionar la carpeta para guardar el archivo normalizado\n\n-> Ingresar en la caja de texto el nombre del archivo normalizado para la seccion de aproximar, la extencion es .txt")
		f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt",title="Ingresa el nombre para el archivo normalizado Aprox. extencion .txt")
		#f.write("Numero de Clases: " + str(len(self.b))+"\n")
		cont=0
		vecAux=[]

		while cont < len(self.X[0]):

			for i in range(len(self.X)):
				f.write(str(self.X[i][cont])+",")
			f.write("\n")
			cont=cont+1
		f.close() # `()` was missing

	def normalizar(self):
		norm=FuncionNormalizar()
		for pos in range(len(self.X)):
			#if pos >=1:
			self.X[pos] =norm.main(self.X[pos])
		self.GuardarDatos()



#iniciar=NormalizaAproximar()
#nombre=iniciar.abrirArchivo()

