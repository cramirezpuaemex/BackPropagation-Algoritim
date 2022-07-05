import sys
from Tkinter import *
import tkMessageBox
from ScrolledText import *
import ttk
import tkFileDialog 
from tkFileDialog import askopenfilename
from Particiones import *
from ParticionesAproximar import *

class ValidacionCruzadaOpcion():
	def ValidacionClasificar(self):
		self.app.destroy()
		#print  ":)"
		work=Particiones()
		work.main()

	def ValidacionAproximar(self):
		self.app.destroy()
		#print  ":)"
		work=ParticionesAproximar()
		work.main()

	def Cancelar(self):
		self.app.destroy()
		#print  ":)"		


	
	
		
	def main(self):
		valor = "" #para el inicio los entry tenga b

		self.app = Tk()
		self.app.title('Validacion Vruzada Opcion.')
		self.app.geometry("300x150")
		self.app.maxsize(300, 150)
		#VP -> VENTANA PRINCIPAL
		self.vp = Frame(self.app)
		
		self.vp.grid(column=0, row=0, padx=(50,50), pady=(10,10)) #posicionar los elementos en tipo matriz, padx es para margen
		self.vp.columnconfigure(0,weight=1)  #tamanio relativo a las columnas
		self.vp.rowconfigure(0,weight=1)



		#NUMERO ITERACIONES
		etiqueta = Label(self.vp,text="El conjunto de Datos contiene clases: ")
		etiqueta.grid(column=0, row=2) 
		
		# #EJECUCION
		boton = Button(self.vp, width=10, text="Si", command=self.ValidacionClasificar)
		boton.grid(column=0,row=5)

		boton1 = Button(self.vp, width=10, text="No", command=self.ValidacionAproximar)
		boton1.grid(column=0,row=7)

		boton2 = Button(self.vp, width=10, text="Cancelar", command=self.Cancelar)
		boton2.grid(column=0,row=30)
		
		


		#CREDITOS
		# etiqueta = Label(vp,text="Elaborado por: CARLOS RAMIREZ PINA")
		# etiqueta.grid(column=1, row=40) 
		self.app.mainloop()
		



