#Desarrollado por Carlos Ramirez Pina
from Tkinter import *
from OpenFile import *
from ClasificarEntrenar import *
from NormalizarOpcion import*
from ValidacionCruzadaOpcion import*
from EntrenarOpcion import*
from TestOpcion import*
from Aproximar import*
from Clasificar import*
import sys



		


class Inter:
	def FuncionClass(self):
		work=FuncionClasificar()
		work.main()
		#print  ":)"

	def Salir(self):
		sys.exit(0)
		##print  texto


	# def ValidacionClasificar(self):
	# 	#print  ":)"
	# 	work=Particiones()
	# 	work.main()
	# def ValidacionAproximar(self):
	# 	#print  ":)"
	# 	work=ParticionesAproximar()
	# 	work.main()


	# def EntrenarClasificar(self):
	# 	inicia=ClasificarEntrenar()
	# 	inicia.main()

	# def EntrenarAproximar(self):
	# 	work=AproximarEntrenar()
	# 	work.main()

	# def TestAproximar(self):
	# 	#print  ":)"
	# 	inicia=AproximarTest()
	# 	inicia.main()
	# def TestClasifica(self):
	# 	inicia=ClasificaTest()
	# 	inicia.main()
	def OpcionesNormalizar(self):
		#tkMessageBox.showinfo("El archivo debe tener extencion .txt, los atributos son separados por comas, la clase o valor esperado es el ultimo atributoy salto de linea")
		tkMessageBox.showinfo("Tipo de archivo", "-> El archivo debe tener extencion .txt\n\n ->Los atributos son separados por comas\n\n -> La clase o valor esperado es el ultimo atributo, seguido de un salto de linea\n\n -> Las clases van de 0,1,2,..,N")
		inicia=NormalizarOpcion()
		inicia.main()		

	def OpcionesValidacionCruzada(self):
		#tkMessageBox.showinfo("El archivo debe tener extencion .txt, los atributos son separados por comas, la clase o valor esperado es el ultimo atributoy salto de linea")
		tkMessageBox.showinfo("Tipo de archivo", "    Para realizar la VALIDACION\n\t   CRUZADA  \n\n -> Los datos tienen que estar normalizados\n\n -> En caso que el archivo no este normalizado VER LA OPCION NORMALIZAR")
		inicia=ValidacionCruzadaOpcion()
		inicia.main()
	def OpcionesEntrenar(self):
		#tkMessageBox.showinfo("El archivo debe tener extencion .txt, los atributos son separados por comas, la clase o valor esperado es el ultimo atributoy salto de linea")
		tkMessageBox.showinfo("Tipo de archivo", "Para realizar el ENTRENAMIENTO\n\n -> Los datos tienen que estar normalizado\n\n -> En caso que el archivo no este normalizado VER LA OPCION NORMALIZAR\n\n -> Se deben de seleccionar archivos de entrenamiento generados de la opcion VALIDACION CRUZADA \n")
		inicia=EntrenarOpcion()
		inicia.main()
	def OpcionesTest(self):
		#tkMessageBox.showinfo("El archivo debe tener extencion .txt, los atributos son separados por comas, la clase o valor esperado es el ultimo atributoy salto de linea")
		tkMessageBox.showinfo("Tipo de archivo", "Para realizar el TEST\n\n -> Se debe de realizar primero el entrenamiento el cual da como resultado un archivo de parametros libres necesarios para realizar el TEST\n\n -> Los datos tienen que estar normalizados\n\n -> En caso que el archivo no este normalizado VER LA OPCION NORMALIZAR\n\n -> Se deben de seleccionar archivos de prueba generados de la opcion VALIDACION CRUZADA \n")
		inicia=TestOpcion()
		inicia.main()
	def Aproximar(self):
		#tkMessageBox.showinfo("El archivo debe tener extencion .txt, los atributos son separados por comas, la clase o valor esperado es el ultimo atributoy salto de linea")
		tkMessageBox.showinfo("Tipo de archivo", "Para aproximar\n\n -> El archivo debe tener extencion .txt\n\n ->Los atributos son separados por comas\n\n ->El ultimo atributo terminara con una coma, seguido de un salto de linea\n\n -> Se debe de realizar primero el entrenamiento el cual da como resultado un archivo de parametros libres necesarios para realizar la proximacion  VER LA OPCION ENTRENAMIENTO\n\n -> Tener el archivo de media y desviacion estandar generado cuando se normalizo los datos para entrenamiento  VER LA OPCION NORMALIZAR\n")
		inicia=Aproximar()
		inicia.main()
	def Clasificar(self):
		#tkMessageBox.showinfo("El archivo debe tener extencion .txt, los atributos son separados por comas, la clase o valor esperado es el ultimo atributoy salto de linea")
		tkMessageBox.showinfo("Tipo de archivo", "Para clasificar\n\n -> El archivo debe tener extencion .txt\n \n->Los atributos son separados por comas\n\n -> El ultimo atributo terminara con una coma, seguido de un salto de linea\n\n -> Se debe de realizar primero el entrenamiento el cual da como resultado un archivo de parametros libres necesarios para realizar la clasificacion VER LA OPCION ENTRENAMIENTO\n\n -> Tener el archivo de media y desviacion estandar generado cuando se normalizo los datos para entrenamiento  VER LA OPCION NORMALIZAR\n")
		inicia=Clasificar()
		inicia.main()	
	def MenuPrincipal(self):
		v0=Tk()
		v0.minsize(166,166)
		v0.title('Sistema CRP')
		menu1 = Menu(v0)
		v0.config(menu=menu1)
		menu1_1 = Menu(menu1, tearoff=0)
		menu1.add_cascade(label="->Opciones<-", menu=menu1_1)
		menu1_1_1 = Menu(menu1_1, tearoff=0)
		menu1_1_2 = Menu(menu1_1, tearoff=0)
		menu1_1_3 = Menu(menu1_1, tearoff=0)
		menu1_1_4 = Menu(menu1_1, tearoff=0)
		menu1_1.add_command(label="Normalizar", command=self.OpcionesNormalizar)
		menu1_1.add_command(label="Valicacion cruzada", command=self.OpcionesValidacionCruzada)	
		#menu1_1_4.add_command(label="Clasificar", command=self.ValidacionClasificar)
		#menu1_1_4.add_command(label="Aproximar", command=self.ValidacionAproximar)
		menu1_1.add_command(label="Entrenamiento", command=self.OpcionesEntrenar)
		#menu1_1_1.add_command(label="Entrenamiento",command=self.EntrenarClasificar)
		#menu1_1_1.add_command(label="Test",command=self.TestClasifica)
		menu1_1.add_command(label="Test", command=self.OpcionesTest)
		menu1_1.add_command(label="Aproximar", command=self.Aproximar)
		menu1_1.add_command(label="Clasificar", command=self.Clasificar)
		#menu1_1_2.add_command(label="Entrenamiento",command=self.EntrenarAproximar)
		#menu1_1_2.add_command(label="Test",command=self.TestAproximar)
		menu1_1.add_command(label="Salir", command=self.Salir)
		
		
		#CREDITOS
		etiqueta = Label(v0,text="Elaborado por: CARLOS RAMIREZ PINA")
		etiqueta.grid(column=0, row=20) 
		tkMessageBox.showinfo("Bienvenido", "En este sistema en el menu OPCIONES podra realizar las siguientes actividades:\n\n -> Normalizar un conjunto de datos\n\n -> Realizar validacion Cruzada\n\n -> Entrenamiento (con el uso del algoritmo Back Propagation)\n\n -> Test(con el uso del algoritmo Back Propagation)\n\n ->Aproximar (conjunto de datos que no se conoce el valor esperado)\n\n ->Clasificar (conjunto de datos que no se conoce la clase asignada)\n\n -> Salir(termino del programa)\n")

		v0.mainloop()	
	def main(self):
		#self.MensajeBienvenida()
		self.MenuPrincipal()

		

iniciar=Inter()
iniciar.main()