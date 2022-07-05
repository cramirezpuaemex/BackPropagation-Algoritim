# Programa de redes neuronales basado en el codigo escrito en C++ de Roberto Alejo Eleuterio
#Desarrollado por Carlos Ramirez Pina
import sys
from Tkinter import *
import tkFileDialog 
import tkMessageBox
from ScrolledText import *
import ttk
from OpenFile import *
from AproximaPrueba import *
import decimal
import random
import math
from tkFileDialog import askopenfilename


class AproximarTest():
	filename = ""
	pathArchivoDE=None
	pathArchivoDF=None
	def pathfileDE(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		self.filename = askopenfilename(title="Abrir archivos de parametros libres para test, Aprox. Debe tener extension .txt") # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
	def pathfileDF(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		self.filename = askopenfilename(title="Abrir archivos de entrenamiento para test, Aprox. Debe tener extension .txt") # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
	def abrirArchivo(self):

		archivo =self.pathfileDE()
		self.etiquetaPath.config(text=archivo)
		self.pathArchivoDE=archivo
		#print  self.pathArchivoDE
	def abrirArchivoFile(self):

		archivo =self.pathfileDF()
		self.etiquetaPath1.config(text=archivo)
		self.pathArchivoDF=archivo
		#print  self.pathArchivoDF
		
	def trabajar(self):
		#print  ":)"
		respuesta=self.validar()
		if respuesta == True:
			##print  " numero de nueronas", self.numeroNeuronas
			tkMessageBox.showinfo("En Proceso", "Preciona OK para continuar\n        Favor de esperar")
			self.app.destroy()
			inicia=AproximaPrueba()
			inicia.main(self.pathArchivoDE, self.pathArchivoDF)


	

	def validar(self):
		valido = False
		##print  'entra'

		#VALIDAR QUE EXITAN PATH SI NO SE SELECCIONO MANUAL
		#if self.pathArchivoDE == None and manualDE == False:
		if self.pathArchivoDE == None:
			valido = False
			tkMessageBox.showinfo("Error", "Debe seleccionar un archivo de datos de entrada")
		elif self.pathArchivoDF == None and manualDES == False:
			valido = False
			tkMessageBox.showinfo("Error", "Debe seleccionar un archivo de datos esperados")
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


		# cadena = "Factor de correccion: " + str(alfa) + "\n" + "Error minimo esperado: " + str(errorminimo) + "\n" + "Error Promedio: " + str(errorpromedio) + "\n"+ "Iteracion: " + str(iteracion) + "\n" + "Error minimo: " + str(minimo) + "\n" + "r1: " + str(ww11) + "\n" + "r2: " + str(uu) + "\n" + "bias: " + str(bb1) + "\n"	+ "bias2:"  + str(bb3) + "\n"
		# result.config(state=NORMAL)
		# result.insert(INSERT, cadena)
		# result.config(state=DISABLED)
	def cambiar_stringvar(nuevotexto,stringvar):
		stringvar.set(nuevotexto)



	def main(self):
		valor = "" #para el inicio los entry tenga b

		self.app = Tk()
		self.app.title('Aproximacion (Test)')
		self.app.geometry("1100x200")
		self.app.maxsize(1100, 200)

		#VP -> VENTANA PRINCIPAL
		vp = Frame(self.app)
		
		vp.grid(column=0, row=0, padx=(50,50), pady=(10,10)) #posicionar los elementos en tipo matriz, padx es para margen
		vp.columnconfigure(0,weight=1)  #tamanio relativo a las columnas
		vp.rowconfigure(0,weight=1)


		#DATOS ENTRADA POR PATH
		etiquetaDE = Label(vp,text="Datos de parametros libres: ")
		etiquetaDE.grid(column=0, row=0) #especificar en la final y columna 
		
		boton = Button(vp, width=21, text="Seleccionar", command=self.abrirArchivo)
		boton.grid(column=2,row=0)

		etiquetaDF = Label(vp,text="Datos de prueba: ")
		etiquetaDF.grid(column=0, row=2) #especificar en la final y columna 
		# v = IntVar()
		# Label(vp,      text="""Choose a programming language:""", justify = LEFT,  padx = 20).pack()
		# Radiobutton(vp, text="Python",padx = 20, variable=v, value=1).pack(anchor=W)
		# Radiobutton(vp, text="Perl",padx = 20, variable=v, value=2).pack(anchor=W)


		
		boton = Button(vp, width=21, text="Seleccionar", command=self.abrirArchivoFile)
		boton.grid(column=2,row=2)
 
		self.etiquetaPath = Label(vp,text=" ")
		self.etiquetaPath.grid(column=1, row=0) 

		self.etiquetaPath1 = Label(vp,text=" ")
		self.etiquetaPath1.grid(column=1, row=2) 
		
		
		
		# #EJECUCION
		boton = Button(vp, width=20, text="Ejecutar", command=self.trabajar)
		boton.grid(column=1,row=8)


	


		botonSalir = Button(vp, width=20, text="Salir", command=self.app.destroy)
		botonSalir.grid(column=2,row=22)
		


		#CREDITOS
		etiqueta = Label(vp,text="Elaborado por: CARLOS RAMIREZ PINA")
		etiqueta.grid(column=1, row=40) 
		self.app.mainloop()



