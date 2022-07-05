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

class NormalizaClasificacion():
	filename = ""
	pathArchivoDE=None
	def pathfile(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		tkMessageBox.showinfo("Tipo de archivo", "Selecciona el archivo de datos que tenga las siguientes caracteristicas:\n\n-> El archivo debe tener extencion .txt\n \n->Los atributos son separados por comas\n \n-> La clase es el ultimo atributo, seguido de un salto de linea\n \n-> Las clases van de 0,1,2,..,N")

		self.filename = askopenfilename(title="Selecciona el archivo para normalizar Clas. extencion .txt") # show an "Open" dialog box and return the path to the selected file
		#print 'pathArchivoDE'
		return(self.filename)
	############################################################################################################################################################################################################
	def abrirArchivo(self):

		archivo =self.pathfile()
		#self.etiquetaPath.config(text=archivo)
		self.pathArchivoDE=archivo
		#print 'abrirArchivo'
		return(self.pathArchivoDE)
		
	############################################################################################################################################################################################################		
	def trabajar(self, nombre):
		print  "aqui si llega, nombre", nombre
		data = self.leerArchivo(nombre)

		self.X = [[] for e in range(len(data[0]))]
		print 'empieza a trabajar'
		#el ultimo vector de X son los valores esperados
		#for i in data:
			#print "len i", len(i)
		#COMENTE ESTE BLOQUE EL DIA 26 DE ABRIR POR LOS DATOS QUE SON MUCHOS
		for conjunto in data:
			for i in range(len(conjunto)):
				self.X[i].append(conjunto[i])
		print "len de self.x", len(self.X[0])
		print "len de x1", len(self.X)
		print  self.X[-1]
		self.normalizar()
	############################################################################################################################################################################################################
	def leerArchivo(self, ruta):
		#print  "aqui si llega, nombre", ruta
		f = open(ruta,"r")
		self.arreglo= []
		contLin=0
		while True:
			linea = f.readline()
			if linea:
				datos = linea.split('\n')
				datos = datos[0].split(',')
				##print  datos
				##print  len(datos) 
				try:
					data = [decimal.Decimal(elemento) for elemento in datos]
					contLin=contLin+1
					print  contLin
					self.arreglo.append(data)
				except Exception, e:
					print  e
			else:
				break
		print 'termina de leer el archivo'
		return self.arreglo

	def GuardarDatos(self):
		############################################################################################################################################################################################################

		tkMessageBox.showinfo("Guardar Archivo Clasificar", "Seleccionar la carpeta para guardar el archivo estadistico (Clas.)\n\n-> Ingresar en la caja de texto el nombre del archivo para la MEDIA y DES. ESTANDAR de cada atributo")
		f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt",title="Ingresa el nombre para el archivo: MEDIA y DES. ESTANDAR (Clasificar). extencion .txt")
		cont=0
		vecAux=[]

		cont0=0
		cont1=0
		rep=0
		for u in range(2):
			Aux=[]
			for i in range(len(self.X)-1):
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
		tkMessageBox.showinfo("Guardar Archivo", "->Seleccionar la carpeta para guardar el archivo normalizar\n\n-> Ingresar en la caja de texto el nombre del archivo normalizado para la seccion de clasificar, la extencion es .txt")
		f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt",title="Ingresa el nombre para el Archivo Normalizado Clas. extencion .txt")
		#f.write("Numero de Clases: " + str(len(self.b))+"\n")
		cont=0
		while cont < len(self.X[0]):

			for i in range(len(self.X)):
				f.write(str(self.X[i][cont])+",")
			f.write("\n")
			cont=cont+1
		f.close() # `()` was missing


	############################################################################################################################################################################################################

	def normalizar(self):
		norm=FuncionNormalizar()
		print "len x", len(self.X)
		print "len X[]", len(self.X[0])
		for pos in range(len(self.X)):
			if pos < len(self.X)-1:
				print "ATRIBUTO: ", pos
				self.X[pos] =norm.main(self.X[pos])
		self.GuardarDatos()



#work=FuncionClasificar()
#work.main()

