import sys
from Tkinter import *
import tkFileDialog 
import tkMessageBox
from ScrolledText import *
import ttk
from OpenFile import *
from EntrenaAproxima import *
import decimal
import random
import math
from tkFileDialog import askopenfilename


class AproximarEntrenar():
	filename = ""
	pathArchivoDE=None
	def pathfile(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		self.filename = askopenfilename(title="Elegir archivo para realizar el entrenamiento Aprox") # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
	def abrirArchivo(self):

		archivo =self.pathfile()
		self.etiquetaPath.config(text=archivo)
		self.pathArchivoDE=archivo
		#print  self.pathArchivoDE
		
	def trabajar(self):
		#print  ":)"
		#VALIDAR FACTOR DE CORRECION TENGA VALOR NUMERICO
		try:
			self.alfa = float(self.entrada_texto.get())
			valido = True
			#VALIDAR FACTOR DE CORRECION TENGA VALOR DENTRO DEL RANGO
			if self.alfa>=0 and self.alfa<=0.9:
				valido = True
			else:
				valido = False
				tkMessageBox.showinfo("Error", "Debe introducir un valor dentro del rango en Factor de correccion")

		except Exception, e:
			valido = False
			tkMessageBox.showinfo("Error", "Debe introducir un valor numerico en Factor de correccion")
		#VALIDAR MOMENTO TENGA VALOR NUMERICO
		try:
			self.Momento = float(self.momento.get())
			valido = True
			#VALIDAR FACTOR DE CORRECION TENGA VALOR DENTRO DEL RANGO
			if self.Momento>=0.2 and self.alfa<=0.4:
				valido = True
			else:
				valido = False
				tkMessageBox.showinfo("Error", "Debe introducir un valor dentro del rango en Factor Momento")

		except Exception, e:
			valido = False
			tkMessageBox.showinfo("Error", "Debe introducir un valor numerico en Factor Momento")
		#*********************************************************************************************
		#VALIDAR NUMERO DE NEURONAS TENGA VALOR NUMERICO
		try:
			self.nNeuronas =  int(self.NoNeurona.get())
			valido = True
			#VALIDAR NUMERO DE ITERACIONES TENGA DENTRO DEL RANGO
			if self.nNeuronas >= 2:
				valido = True
			else:
				valido = False
				tkMessageBox.showinfo("Error", "Debe introducir un valor dentro del rango en numero de neuronas en la capa oculta")

		except Exception, e:
			valido = False
			tkMessageBox.showinfo("Error", "Debe introducir un valor numerico en Numero de neuronas en la capa oculta#")
		#*********************************************************************************************
		#VALIDAR NUMERO DE ITERACIONES TENGA VALOR NUMERICO
		try:
			self.nIteraciones =  int(self.entradaIter.get())
			valido = True
			#VALIDAR NUMERO DE ITERACIONES TENGA DENTRO DEL RANGO
			if self.nIteraciones > 500:
				valido = True
			else:
				valido = False
				tkMessageBox.showinfo("Error", "Debe introducir un valor dentro del rango en numero de iteraciones")

		except Exception, e:
			valido = False
			tkMessageBox.showinfo("Error", "Debe introducir un valor numerico en Numero de iteraciones")



		#VALIDAR MSE TENGA VALOR NUMERICO
		try:
			self.errorminimo =  float(self.entradaMSE.get())
			valido = True
		except Exception, e:
			valido = False
			tkMessageBox.showinfo("Error", "Debe introducir un valor numerico en Error minimo de MSE")
		#print "ya :)"

		##print  " numero de nueronas", self.numeroNeuronas
		if valido == True:
			self.app.destroy()
			tkMessageBox.showinfo("En Proceso", "Preciona OK para continuar\n        Favor de esperar")
			#print  "factor correccion", self.alfa, "momento ", self.Momento, "numero de neuronas", self.nNeuronas,"Iteraciones", self.nIteraciones, "MSE", self.errorminimo
			inicia=EntrenaAproxima()
			inicia.main(self.pathArchivoDE,  self.alfa, self.Momento,self.nNeuronas, self.nIteraciones,self.errorminimo,)



	def validar(self):
		valido = False
		##print  'entra'

		#VALIDAR QUE EXITAN PATH SI NO SE SELECCIONO MANUAL
		#if self.pathArchivoDE == None and manualDE == False:
		if self.pathArchivoDE == None:
			valido = False
			tkMessageBox.showinfo("Error", "Debe seleccionar un archivo de datos de entrada")
		#elif self.pathArchivoDES == None and manualDES == False:
			#valido = False
			#tkMessageBox.showinfo("Error", "Debe seleccionar un archivo de datos esperados")
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
		self.app.title('Aproximar: Entrenamiento utilizando una red neuronal')
		self.app.geometry("1100x500")
		self.app.maxsize(1100, 500)

		#VP -> VENTANA PRINCIPAL
		vp = Frame(self.app)
		
		vp.grid(column=0, row=0, padx=(50,50), pady=(10,10)) #posicionar los elementos en tipo matriz, padx es para margen
		vp.columnconfigure(0,weight=1)  #tamanio relativo a las columnas
		vp.rowconfigure(0,weight=1)


		#DATOS ENTRADA POR PATH
		etiquetaDE = Label(vp,text="Datos de entrada: ")
		etiquetaDE.grid(column=0, row=0) #especificar en la final y columna 
		
		boton = Button(vp, width=21, text="Seleccionar", command=self.abrirArchivo)
		boton.grid(column=2,row=0)

 
		self.etiquetaPath = Label(vp,text=" ")
		self.etiquetaPath.grid(column=1, row=0) 
		
		
		
		#ENTRENAMIENTO
		# self.botonEntrenar = Button(vp, width=20, text="Entrenar", command=self.Entrenar)
		# self.botonEntrenar.grid(column=3,row=17)
		# self.botonEntrenar.config(state=DISABLED)
		#FACTOR DE CORRECCION
		etiqueta = Label(vp,text="Factor de correccion (0 - 0.9): ")
		etiqueta.grid(column=0, row=4) 
		self.entrada_texto = Entry(vp,width=20,textvariable=valor) #unidaes relativas
		self.entrada_texto.grid(column=1,row=4)
		#self.entrada_texto.config(state=DISABLED)
		#**********************************************************************************************
		#Momento
		etiqueta = Label(vp,text="Momento (valores recomendados 0.2 - 0.4): ")
		etiqueta.grid(column=0, row=5) 
		self.momento= Entry(vp,width=20,textvariable=valor) #unidaes relativas
		self.momento.grid(column=1,row=5)
		#self.entrada_texto.config(state=DISABLED)
		#***********************************************************************************************
		#NUMERO DE NEURONAS
		etiqueta = Label(vp,text="Numero de neruonas en la capa oculta (>2): ")
		etiqueta.grid(column=0, row=6) 
		
		self.NoNeurona = Entry(vp,width=20,textvariable=valor) #unidaes relativas
		self.NoNeurona.grid(column=1,row=6)



		#NUMERO ITERACIONES
		etiqueta = Label(vp,text="Numero de iteraciones (>500): ")
		etiqueta.grid(column=0, row=7) 
		
		self.entradaIter = Entry(vp,width=20,textvariable=valor) #unidaes relativas
		self.entradaIter.grid(column=1,row=7)


		#self.entradaIter.config(state=DISABLED)
		#ERROR CUADRATICO MEDIO
		etiqueta = Label(vp,text="Error minimo de MSE(Recomendado: 0.0001) : ")
		etiqueta.grid(column=0, row=8) 
		
		self.entradaMSE = Entry(vp,width=20,textvariable=valor) #unidaes relativas
		self.entradaMSE.grid(column=1,row=8)
		#self.entradaMSE.config(state=DISABLED)

		# #EJECUCION
		boton = Button(vp, width=20, text="Ejecutar", command=self.trabajar)
		boton.grid(column=1,row=10)
		
		
		# etiquetaR = Label(vp,text="RESULTADOS ")
		# etiquetaR.grid(column=1, row=12) #2,16
		# self.result = ScrolledText(vp, width=50, height=10) #width caracteres height lineas
		# self.result.grid(column=1,row=14)#2,18
		
		#self.result.config(state=DISABLED)

		#Guarda informacion del conjunto de datos
		# self.botonGuardar = Button(vp, width=20, text="Guardar Informacion de datos", command=self.GuardarDatos)
		# self.botonGuardar.grid(column=1,row=20)
		# self.botonGuardar.config(state=DISABLED)



	


		botonSalir = Button(vp, width=20, text="Salir", command=self.app.destroy)
		botonSalir.grid(column=2,row=22)
		


		#CREDITOS
		etiqueta = Label(vp,text="Elaborado por: CARLOS RAMIREZ PINA")
		etiqueta.grid(column=1, row=40) 
		self.app.mainloop()



