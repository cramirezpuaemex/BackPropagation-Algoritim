import sys
from Tkinter import *
import tkMessageBox
from ScrolledText import *
import ttk
from OpenFile import *
from GuardaValor import*
import decimal
import random
import math
import tkFileDialog 
from tkFileDialog import askopenfilename
from FuncionNormalizar import *

class Particiones():
	
	def trabajar(self):
		##print  ":)"
		#VALIDAR NUMERO DE ITERACIONES TENGA VALOR NUMERICO
		try:
			self.particiones =  decimal.Decimal(self.entradaIter.get())
			valido = True
			#VALIDAR NUMERO DE ITERACIONES TENGA DENTRO DEL RANGO
			if self.particiones > 0:
				valido = True
			else:
				valido = False
				tkMessageBox.showinfo("Error", "Debe introducir un valor dentro del rango de particiones")

		except Exception, e:
			valido = False
			tkMessageBox.showinfo("Error", "Debe introducir un valor numerico en particiones")

		##print  "particiones",
		if valido == True:
			self.app.destroy()
			guarda=GuardaValor()
			guarda.main(self.particiones)




	def Cancelar(self):
		self.app.destroy()
		#print  ":)"		
		
	def main(self):
		valor = "" #para el inicio los entry tenga b

		self.app = Tk()
		self.app.title('Numero de particiones para Clasificar')
		self.app.geometry("400x100")
		self.app.maxsize(400, 100)

		#VP -> VENTANA PRINCIPAL
		self.vp = Frame(self.app)
		
		self.vp.grid(column=0, row=0, padx=(50,50), pady=(10,10)) #posicionar los elementos en tipo matriz, padx es para margen
		self.vp.columnconfigure(0,weight=1)  #tamanio relativo a las columnas
		self.vp.rowconfigure(0,weight=1)



		#NUMERO ITERACIONES
		etiqueta = Label(self.vp,text="Numero de Particiones > 0: ")
		etiqueta.grid(column=0, row=5) 
		
		self.entradaIter = Entry(self.vp,width=15,textvariable=valor) #unidaes relativas
		self.entradaIter.grid(column=1,row=5)
		#self.entradaIter.config(state=DISABLED)

		# #EJECUCION
		boton = Button(self.vp, width=15, text="Ejecutar", command=self.trabajar)
		boton.grid(column=0,row=10)

		boton1 = Button(self.vp, width=15, text="Cancelar", command=self.Cancelar)
		boton1.grid(column=1,row=10)		
		


		#CREDITOS
		# etiqueta = Label(vp,text="Elaborado por: CARLOS RAMIREZ PINA")
		# etiqueta.grid(column=1, row=40) 
		self.app.mainloop()
		



