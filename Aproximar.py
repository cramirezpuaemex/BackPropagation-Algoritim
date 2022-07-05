# Programa de redes neuronales basado en el codigo escrito en C++ de Roberto Alejo Eleuterio
#Desarrollado por Carlos Ramirez Pina
import sys
from Tkinter import *
import tkFileDialog 
import tkMessageBox
from ScrolledText import *
import ttk
from OpenFile import *
from ResultadosAproximarNew import *
import decimal
import random
import math
from tkFileDialog import askopenfilename


class Aproximar():
	filename = ""
	pathArchivoDE=None
	pathArchivoDF=None
	pathArchivoDA=None
	def pathfilePL(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		self.filename = askopenfilename(title="Ingresa el archivo que contiene los parametros libres obtenidos del entrenamiento Aprox") # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
	def pathfileME(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		self.filename = askopenfilename(title="Ingresa el archivo que contiene la media y desviacion estandar obtenido de la normalizacion Aprox") # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
	def pathfileAN(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		self.filename = askopenfilename(title="Ingresa el archivo que contiene los datos para realizar la proximacion") # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
	def abrirArchivo(self):

		archivo =self.pathfilePL()
		self.etiquetaPath.config(text=archivo)
		self.pathArchivoDE=archivo
		print  self.pathArchivoDE
	def abrirArchivoFile(self):

		archivo1 =self.pathfileME()
		self.etiquetaPath1.config(text=archivo1)
		self.pathArchivoDF=archivo1
		print  self.pathArchivoDF

	def abrirArchivoDatos(self):

		archivo2=self.pathfileAN()
		self.etiquetaPath2.config(text=archivo2)
		self.pathArchivoDA=archivo2
		print  self.pathArchivoDA
		
	def trabajar(self):
		#print  ":)"
		respuesta=self.validar()
		if respuesta == True:
			##print  " numero de nueronas", self.numeroNeuronas
			tkMessageBox.showinfo("En Proceso", "Preciona OK para continuar\n        Favor de esperar")
			self.app.destroy()
			print " vamos bien :)"
			inicia=ResultadosAproximarNew()
			inicia.main(self.pathArchivoDE, self.pathArchivoDF, self.pathArchivoDA)


	

	def validar(self):
		valido = False
		##print  'entra'

		#VALIDAR QUE EXITAN PATH SI NO SE SELECCIONO MANUAL
		#if self.pathArchivoDE == None and manualDE == False:
		if self.pathArchivoDE == None:
			valido = False
			tkMessageBox.showinfo("Error", "Debe seleccionar un archivo de parametros libres")
		elif self.pathArchivoDF == None:
			valido = False
			tkMessageBox.showinfo("Error", "Debe seleccionar un archivo de media y desviacion estandar")
		elif self.pathArchivoDA == None:
			valido = False
			tkMessageBox.showinfo("Error", "Debe seleccionar un archivo de datos para aproximar")
		else:
			valido = True

		return valido


	def habilitarManual(self):
		if len(self.b)!=0:
			self.botonGuardar.config(state=NORMAL)



	def habilitarDataSet(self, long):
		if long !=0:
			self.entrada_texto.config(state=NORMAL)
			self.entradaIter.config(state=NORMAL)
			self.entradaMSE.config(state=NORMAL)
			self.botonEntrenar.config(state=NORMAL)

	def cambiar_stringvar(nuevotexto,stringvar):
		stringvar.set(nuevotexto)



	def main(self):
		valor = "" #para el inicio los entry tenga b

		self.app = Tk()
		self.app.title('Aproximacion (Datos sin el valor esperado)')
		self.app.geometry("1100x200")
		self.app.maxsize(1100, 200)

		#VP -> VENTANA PRINCIPAL
		vp = Frame(self.app)
		
		vp.grid(column=0, row=0, padx=(50,50), pady=(10,10)) #posicionar los elementos en tipo matriz, padx es para margen
		vp.columnconfigure(0,weight=1)  #tamanio relativo a las columnas
		vp.rowconfigure(0,weight=1)


		#DATOS ENTRADA POR PATH
		etiquetaDE = Label(vp,text="Archivo de parametros libres: ")
		etiquetaDE.grid(column=0, row=0) #especificar en la final y columna 
		
		boton = Button(vp, width=21, text="Seleccionar", command=self.abrirArchivo)
		boton.grid(column=2,row=0)
		#######################################################################################
		etiquetaDF = Label(vp,text="Archivo de media y desviacion Estandar: ")
		etiquetaDF.grid(column=0, row=2) #especificar en la final y columna 

		boton = Button(vp, width=21, text="Seleccionar", command=self.abrirArchivoFile)
		boton.grid(column=2,row=2)
 		########################################################################################
				#######################################################################################
		etiquetaDA = Label(vp,text="Archivo de los datos para aproximar: ")
		etiquetaDA.grid(column=0, row=3) #especificar en la final y columna 

		boton = Button(vp, width=21, text="Seleccionar", command=self.abrirArchivoDatos)
		boton.grid(column=2,row=3)
 		########################################################################################

		self.etiquetaPath = Label(vp,text=" ")
		self.etiquetaPath.grid(column=1, row=0) 

		self.etiquetaPath1 = Label(vp,text=" ")
		self.etiquetaPath1.grid(column=1, row=2) 
		
		self.etiquetaPath2 = Label(vp,text=" ")
		self.etiquetaPath2.grid(column=1, row=3) 
		
		
		# #EJECUCION
		boton = Button(vp, width=20, text="Ejecutar", command=self.trabajar)
		boton.grid(column=1,row=8)


	


		botonSalir = Button(vp, width=20, text="Salir", command=self.app.destroy)
		botonSalir.grid(column=2,row=22)
		


		#CREDITOS
		etiqueta = Label(vp,text="Elaborado por: CARLOS RAMIREZ PINA")
		etiqueta.grid(column=1, row=40) 
		self.app.mainloop()



