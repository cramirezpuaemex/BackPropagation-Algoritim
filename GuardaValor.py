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
class GuardaValor():
	filename = ""
	pathArchivoDE=None
	def pathfile(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		self.filename = askopenfilename(title="Selecciona el archivo normalizado para validacion cruzada (Clasificar).") # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
	def abrirArchivo(self):

		archivo =self.pathfile()
		#self.etiquetaPath.config(text=archivo)
		self.pathArchivoDE=archivo
		return(self.pathArchivoDE)
	def leerArchivo(self, ruta):
		#print  "aqui si llega, nombre", ruta
		f = open(ruta,"r")
		self.arreglo= []
		while True:
			linea = f.readline()

			if linea:
				datos = linea.split('\n')
				datos = datos[0].split(',')
				#print  datos
				##print  len(datos) 
				try:
					data = [decimal.Decimal(datos[elemento]) for elemento in range(len(datos)-1)]
					##print  data

					self.arreglo.append(data)
				except Exception, e:
					print  e
			else:
				break
		return self.arreglo

	def trabajar(self, nombre):
		#print  "aqui si llega, nombre--------------", nombre
		data = self.leerArchivo(nombre)
		self.X = [[] for e in range(len(data[0]))]

		#el ultimo vector de X son los valores esperados

		for conjunto in data:
			for i in range(len(conjunto)):
				self.X[i].append(conjunto[i])
		#print  self.X
		##print  "data", data


		self.validacionCruzada()
	def validacionCruzada(self):
		clases=self.X[-1]
		self.b=[]
		self.c=[]
		for i in clases:
			if len(self.b)==0:
				self.b.append(i)
				self.c.append(1)
			else:
				if i in self.b:
					self.c[self.b.index(i)]=self.c[self.b.index(i)]+1
				else:
					self.b.append(i)
					self.c.append(1)
		vectoraux=[]
		self.entrenamiento=[]
		self.test=[]
		for i in range(len(self.c)):
			vectoraux.append(0)

		##print  "len(self.c)", len(self.c)
		##print  "len(vectoraux)", len(vectoraux)

		##print  "vect b", self.b
		##print  "vect c", self.c
		##print  "vec vecaux", vectoraux
		##print  'X', self.X
		#rutadeldirectorio=tkFileDialog.askdirectory(title="Select A Folder")
		#print  self.rutadeldirectorio
		
		#while contParticiones < self.numparticiones:
		while len(self.X[-1])!=0:
		 	file=[]
		 	file1=[]
		 	poss=random.randint(0,len(self.X[-1])-1)
		 	##print  "posicion", poss

		 	val=self.X[-1][poss]
		 	##print  "valor", val

			indexVal=self.b.index(val)
			##print  "indexVal", indexVal

			if vectoraux[indexVal] < (self.c[indexVal]*80)/100:
				for i in range(len(self.X)):
					file.append(self.X[i][poss])
				vectoraux[indexVal] = vectoraux[indexVal] + 1
				##print  file

				#ELIMINACION DE LINEA
				for i in range(len(self.X)):
					del self.X[i][poss]
			else:
				for i in range(len(self.X)):
					file1.append(self.X[i][poss])

				#ELIMINACION DE LINEA
				for i in range(len(self.X)):
					del self.X[i][poss]
			##print  "vect c", self.c
			##print  "vec vecaux", vectoraux
			if len(file)!=0:
				self.entrenamiento.append(file)
			if len(file1)!=0:
					self.test.append(file1)
			###print  "len(self.X[0])",len(self.X[0])

			##print  self.entrenamiento
			
			#print  "vector clases", self.b

			fo = open(self.rutadeldirectorio+'/entrenamiento'+str(self.contParticiones)+'.txt', 'w')
			##print >>fo,PW,'\n', PB, '\n', PU, '\n', PB1
			for i in self.entrenamiento:
				for j in i:
					fo.write(str(j)+",")
				fo.write("\n")	
 			#print  ":)"
 			fo.close() 
			fo = open(self.rutadeldirectorio+'/test'+str(self.contParticiones)+'.txt', 'w')
			##print >>fo,PW,'\n', PB, '\n', PU, '\n', PB1
			for i in self.test:
				for j in i:
					fo.write(str(j)+",")
				fo.write("\n")		
 			#print  ":)"
 			fo.close() 	 				
 			#contParticiones=contParticiones+1

	def main(self, valor):
		self.contParticiones=0
		self.numparticiones=valor
		
		self.nombre=self.abrirArchivo()
		#print  self.nombre
		self.rutadeldirectorio=tkFileDialog.askdirectory(title="Selecciona Carpeta para guardar archivos de prueba y entrenamiento")
		while self.contParticiones < self.numparticiones:
			self.trabajar(self.nombre)
			self.contParticiones=self.contParticiones+1