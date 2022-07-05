# Programa de redes neuronales basado en el codigo escrito en C++ de Roberto Alejo Eleuterio
#Desarrollado por Carlos Ramirez Pina
import copy
from Tkinter import*
import math
import tkMessageBox
import matplotlib.pyplot as plt
import tkFileDialog 
from tkFileDialog import askopenfilename
import sys

class ResultadosClasificarNew():
	def leerArchivoRed(self, ruta):
		f = open(ruta,"r")
		arreglo= []
		while True:
			linea = f.readline()
			if linea:
				datos = linea.split(',\n')
				datos = datos[0].split(',')
				##print   datos, "\n"
				##print  len(datos) 
				try:
					data = [(elemento) for elemento in datos]
					##print  data

					arreglo.append(data)
				except Exception, e:
					print  e
			else:
				break
		##print  arreglo
		return arreglo
	def leerArchivoEstadisticos(self, ruta):
		f = open(ruta,"r")
		arreglo= []
		while True:
			linea = f.readline()
			#print "linea", linea
			if linea:
				datos = linea.split(',\n')
				datos = datos[0].split(',')
				#print   datos, "\n"
				##print  len(datos) 
				try:
					data = [float(elemento) for elemento in datos]
					##print  data

					arreglo.append(data)
				except Exception, e:
					print  e
			else:
				break
		#print  arreglo
		return arreglo
	def lecturaArchivo(self, ruta):
		f = open(ruta,"r")
		elementos= []
		while True:
			linea = f.readline()
			if linea:
				elementos.append(linea)
			else:
				break
		#for i in elementos:
			#print  i
		##
		print  elementos
		self.elementos1 = []
		for i in elementos:
			lista=i.split(",")
			lista.remove("\n")
		 	self.elementos1.append([(e) for e in lista])
		 	#lista1=lista.split("\n")
		 	#self.elementos1.append(lista)
		self.Q=len(self.elementos1)
		self.N=len(self.elementos1[0])+1
		self.X=[]
		#for i in self.elementos1:
			#print "patron", i
		self.elementos2=[]
		for u in range(len(self.elementos1)):
			aux=[]
			for i in range(len(self.elementos1[u])):
				aux.append(float(self.elementos1[u][i]))
			self.elementos2.append(aux)
		#for i in self.elementos2:
			#print "patron", i		
		self.normalizar()
		##print  self.elementos1[0][0]
		##print  "Q", self.Q
		##print  "jjkhjkhjkhjk", len(self.elementos1[0])
		# tkMessageBox.showinfo("Guardar Archivo", "Seleccionar la carpeta donde sera almacenado, ingresar en la caja de texto el nombre del archivo normalizado para la seccion de aproximar, la extencion es .txt")
		# f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt",title="Ingresa el nombre para el archivo normalizado  sin el valor esperado, Aprox. extencion .txt")
		# #f.write("Numero de Clases: " + str(len(self.b))+"\n")
		# cont=0
		# vecAux=[]
		# for u in range(len(self.elementos2)):
		# 	for i in range(len(self.elementos2[u])-1):
		# 		f.write(str(self.elementos2[u][i])+",")
		# 	#f.write(str(0))
		# 	f.write("\n")
		# 	cont=cont+1

		# f.close() # `()` was missing

		#########################################
		for i in range(self.Q):
			aux=[]
			for j in range(self.N-1):
				##print  "i", i,"j", j 
				aux.append(float(self.elementos2[i][j]))
			aux.append(1)#se le aumenta el bias
			aux.append(float(self.elementos2[i][-1]))# se le asigna la clase
			self.X.append((aux))
			
		self.N=self.N #Se le suma el bias
		#self.NoClases()
		#print  "numero de atributos", self.N, "no patrones", self.Q,"numero de clases o salidas", self.J, "numero de neuronas", self.M
		##print  "self.ptrxcls", self.ptrxcls
		#for i in self.X:
			#print  i
	def NoClases(self):

		#clases=self.X
		#self.b=[0]
		# for i in clases:
		# 	if len(self.b)==0:
		# 		self.b.append(i[-1])
		# 	else:
		# 		if i[-1] not in self.b:
		# 			self.b.append(i[-1])
					
		#self.b.sort()
		#print  "b", self.b
		#self.J=len(self.b)
		# self.ptrxcls=[0 for i in range(self.J)]
		# for i in clases:
		# 	pos=i[-1]
		# 	##print  pos
		# 	self.ptrxcls[pos]=self.ptrxcls[pos]+1




		#self. netNeural()

		print  "numero de atributos", self.N, "no patrones", self.Q,"numero de clases o salidas", self.J, "numero de neuronas", self.M
		##print  "self.ptrxcls", self.ptrxcls
		for i in self.X:
			print  i
		##print  self.X[1]

	def leerDatosRed(self):
		data = self.leerArchivoRed(self.pathArchivoRED)
		#En data estan los valores de los parametros libres de la red(W, bias, U, bias1), la media y desviacion estandar para la normalizacion de los datos
		##print  len(data)
		#En data1 se encuentran los vectores de para realizar las pruebas
		#data1=leerArchivo
		#Manda a la funcion Predecir para realizar las pruebas
		#Predecir(data, X)
		aux1=[]
		aux2=[]
		aux=0
		self.W=[]
		self.U=[]
		self.M=int(data[0][0])
		self.J=int(data[0][1])
		for i in data[1]:
			if aux < (self.M):
				aux1.append(float(i))
				aux=aux+1
			else:
				aux=1
				self.W.append(aux1)
				aux1=[]
				aux1.append(float(i))
		self.W.append(aux1)

		# for i in self.W:
		# 	print  "i", i

		# aux=0
		# #print  "fsdf", data[2]
		# for i in range(len(data[2])):
		# 	aux2=[]
		# 	aux2.append	(float(data[2][i]))
		# 	self.U.append(aux2)
		# for i in self.U:
		# 	print  "u",i

		aux=0
		for i in data[2]:
			if aux < (self.J):
				aux2.append(float(i))
				aux=aux+1
			else:
				aux=1
				self.U.append(aux2)
				aux2=[]
				aux2.append(float(i))
		self.U.append(aux2)


		# print  "pesos W", len(self.W),"x", len(self.W[0])
		# for i in self.W:
		# 	print  i
		# print  "pesos U", len(self.U),"x", len(self.U[0])
		# for i in self.U:
		# 	print  i
		# print  "numero de neuronas", self.M
	#/***************************************************************************/
	def leerDatosEstadisticos(self):
		data1 = self.leerArchivoEstadisticos(self.pathArchivoEstadisticos)
		#En data estan los valores de los parametros libres de la red(W, bias, U, bias1), la media y desviacion estandar para la normalizacion de los datos
		##print  len(data)
		#En data1 se encuentran los vectores de para realizar las pruebas
		#data1=leerArchivo
		#Manda a la funcion Predecir para realizar las pruebas
		#Predecir(data, X)

		#print data1
		aux1=[]
		self.Media=[]
		self.DesviacionEstandar=[]
		for i in range (len(data1)):
			for j in data1[i]:
				if i ==0:
					self.Media.append(round(j, 3))
				else:
					self.DesviacionEstandar.append(round(j, 3))

		#self.M=int(data[0][0])
		#print "media ", self.Media
		#print "desviacion", self.DesviacionEstandar

	#/***************************************************************************/


 	def normalizar(self):
 		a=len(self.elementos2[0])
 		b=len(self.Media)
 		c=len(self.DesviacionEstandar)
 		#b=b-1
 		#c=c-1
 		#print "len de self.X", a
 		#print "len de self.m", b
 		#print "len de self.d", c

 		if a== b and a==c:

 			for e in range(len(self.elementos2)):
 				for j in range(len(self.elementos2[e])):
					self.elementos2[e][j]=round(self.sigmoide((self.elementos2[e][j]-self.Media[j])/self.DesviacionEstandar[j]),3)
				self.elementos2[e].append(0)
			#for i in self.elementos2:
				#print "patron normalizado", i
		else:
			tkMessageBox.showinfo("Error", "los archivos no tienen los mismos atributos,favor de revisarlos")
			sys.exit(0)
	#/***************************************************************************/
	def initPtrXcls(self):
		self.ptrxcls=[]
		for j in range(self.J):
			self.ptrxcls.append(0)

	#/***************************************************************************/
	def initConf(self):# //Inicializa la matriz de confusion
		#for (int j=0;j<J;j++)
		self.conf=[]
		for j in range(self.J):
			#for (int jj=0;jj<J;jj++)
			aux=[]
			for jj in range(self.J):
	 			aux.append(0)	
	 		self.conf.append(aux)

	#/**************************************************************************/	
	def getAcc(self):# //Obtiene los valores para la matriz de confusion
		for q in range(self.Q):
			self.forwardW(q)
			self.conf[self.getValMaxZ()][self.getValMaxT()]=self.conf[self.getValMaxZ()][self.getValMaxT()]+1
		
		#/***************************************************************************/
	def getValMaxZ(self): #{ //Obtine la clase real de la muestra "q"
		Max=self.z[0]
		clss=0
		for j in range(self.J):
		#for(int j=1;j<J;j++)
			if(self.z[j]>Max):
				##print  self.z[j]
				Max =self.z[j]
				clss =j
		##print  "clss", clss
		return clss
	

	#/***************************************************************************/
	def getValMaxT(self): #{ //Obtine la clase deseada de la muestra "q"
		Max=self.t[0]
		clss=0
		for j in range(self.J):
		#for(int j=1;j<J;j++)
			if(self.t[j]>Max):
				Max =self.t[j]
				clss =j

			       
		return clss
	def forwardW(self, q):# //Propaga los valores desde la capa de entrada hasta la capa de salida
		self.y=[]
		#for(int m=0;m<M;m++)
		for m in range(self.M):
			self.y.append(0)

		#for(int m=0;m<M;m++)
		for m in range(self.M):
			#for(int n=0;n<N;n++)
			for n in range(self.N):
				self.y[m]=self.y[m]+self.X[q][n]*self.W[n][m]
		for m in range(self.M): #mas 1 del bias
		#for(int m=0;m<M+1;m++)//mas 1 de bias;
			self.y[m]= self.sigmoide(self.y[m])

		self.y.append(1) #agrega el bias
		##print  self.y
		self.forwardU(q)
		self.desiredOutput(q)

	#/***************************************************************************/
	def forwardU(self, q):#{ //Propaga los valores desde la capa oculta hasta la salida de la red
		self.z=[]
		
		for j in range(self.J):
		#for(int j=0;j<J;j++)
			self.z.append(0)
		for j in range(self.J):
		#for(int j=0;j<J;j++)
			for  m in range(self.M+1):# mas 1 de bias
			#for(int m=0;m<M+1;m++)//mas 1 de bias
				self.z[j]=self.z[j]+self.U[m][j]*self.y[m]
		for j in range(self.J):
		#for(int j=0;j<J;j++)
			self.z[j] = self.sigmoide(self.z[j])
		##print  "resultado de la red", self.z
		self.guardaZ.append(self.z)		
	#/***************************************************************************/
	def sigmoide(self, net):
		exp=(2.718281)
		resultado=((1)/(1+pow((exp),(-net))))
		return resultado	
	#/***************************************************************************/
	def desiredOutput(self, q):#{ //Determina la salida deseada de la muestra "q"
		self.t=[]
		
		##print  "clase ", self.X[q][-1]
		for j in range(self.J):
		#for(int j=0;j<J;j++){
			if (self.X[q][-1]== j):
				self.t.append(0.9)
			else:
				self.t.append(0.1)	
		##print  "valores esperados", self.t
		self.guardaT.append(self.t)
	#/***************************************************************************/
	def printConf(self): #//Imprime los valores de la matriz de confusion 
		#print  ":)"
		#print  len(self.X), len(self.X[0])
		f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
		
		sumaTotal=0
		precisionGeneral=0
		precisionClase=[]
		#print  "Matrix De confusion"
		for j in range(self.J+1):
			if j==0:
				f.write("\t")
			else:
				f.write("clase "+str(j-1)+"\t")
			f.write("\t")
		f.write("\n")
		for j in range(self.J):
			#for(int jj=0;jj<J;jj++)
			f.write("clase "+str(j)+" \t")
			for jj in range(self.J):
				f.write(str(self.conf[j][jj])+"\t\t")
			
				
				##print  j,"-", jj
				if j==jj:
					precisionClase.append(self.conf[j][jj])
					sumaTotal=sumaTotal+self.conf[j][jj]
			f.write("\n")
		f.write("\n")
		f.write("\n")
		#print  "sumaTotal", sumaTotal, "Q",self.Q
		precisionGeneral=float(sumaTotal)/self.Q
		auxMG=1
		aux=0
		for j in range(self.J):
			aux=float(precisionClase[j])/self.copyptrcls[j]
			f.write("precision de la clase "+ str(j)+" es "+str(aux))
			f.write("\n")
			auxMG=auxMG*((float(precisionClase[j])/self.copyptrcls[j]))
		MediaGeometrica=math.sqrt(auxMG)
		f.write ("media geometrica:  "+str(MediaGeometrica)+"\n")
		f.write ("precision General: "+str( precisionGeneral))
		f.close() # `()` was missing
		
		#print ("\n")	
	#/***************************************************************************/
	def printZandT(self):
		#for(int q=1;q<Q;q++)
		tkMessageBox.showinfo("Guardar Archivo", "Seleccionar la carpeta e ingresar en la caja de texto el nombre del archivo con los resultados para la seccion de clasificar, la extencion es .txt")
		fo = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt", title="Ingresa el nombre para el archivo Resultados Clas. Debe tener extension .txt")	
		fo.write("patrones con el valor aproximado al final de cada patron\n")
		classe=[]
		for q in range(self.Q):
			#print self.guardaT[q],
			#print"<-->  ",
			classe.append(self.guardaZ[q].index(max(self.guardaZ[q])))
			#print "\n"


		cont=0
		vecAux=[]
		for u in range(len(self.elementos1)):
			for i in range(len(self.elementos1[u])):
				f.write(str(self.elementos1[u][i])+",")
			f.write(str(classe[u]))
			f.write("\n")
			cont=cont+1

		f.close() # `()` was missing
	# def printZandT(self):
	# 	#for(int q=1;q<Q;q++)
	# 	promedio=0
	# 	fo = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt", title="Ingresa el nombre para el archivo Resultados Aprox. Debe tener extension .txt")	
	# 	fo.write("patrones con el valor aproximado al final de cada patron\n")

	# 	for i in range(len(self.guardaZ)):
	# 		for j in range(len(self.X[i])-2):
	# 			fo.write(str(self.X[i][j])+",")
	# 		fo.write(str(round(self.guardaZ[i],3))+"\n")		



	# 	# fo.write("Datos esperados\t<-->\tDatos aproximados\n")
	# 	# for q in range(self.Q):
	# 	# 	fo.write( str(self.guardaT[q]))
	# 	# 	fo.write("\t\t<-->\t"),
	# 	# 	fo.write( str(self.guardaZ[q]))
	# 	# 	fo.write( "\n")
	# 	# 	promedio=promedio+abs(self.guardaT[q]-self.guardaZ[q])
	# 	# PromedioPrecision=promedio/self.Q

	# 	# fo.write("precision promedio  " + str(PromedioPrecision))
 # 		#print  ":)"
 # 		fo.close()
			
	#/***************************************************************************/
	def main(self, parametrosLibres, mediaDesviacion, ArchivoPrueba):
		#self.eta = 0.1 #Razon de aprendizaje o learning rate
		#self.mu =0.3 #Momento 
		self.N=0 #no. atributos 
		self.Q=0 #no. de patrones
		self.J=0 #no. de clases o salidas
		self.guardaT=[]
		self.guardaZ=[]
		#self.M=3 #no. de neuronas ocultas
		# self.I=10000 #no. de iteraciones
		# self.maxQ=52000 #maximo numero de patrones
		# self.maxN=210 #maximo numero de atributos
		# self.maxM=100 #maximo numero de neuronas ocultas
		# self.maxJ=15 #maximo numero de clases o salidas
		#self.mse #error cuadratico medio global
		# self.contErrores=[]
		# self.msexcls=[]
		#self.ptrxcls=[]
		self.pathArchivoEstadisticos=mediaDesviacion
		self.pathArchivoRED=parametrosLibres
		self.leerDatosRed()
		self.leerDatosEstadisticos()
		self.lecturaArchivo(ArchivoPrueba)
		#self.normalizar()
		# self.setUp()
		# self.learning()
		# self.imprimirArchivo()
		# self.grafica()
		#self.getAcc()
		#self.#print Conf()

		#/*****************************************
		#    *           FASE DE CONTROL             *
		#    ****************************************/       
		self.initConf() #//limpiar ptrsxcls y matriz de confusion 
		self.initPtrXcls()
   		self.getAcc()
   		self.printZandT()
   		#-----self.Grafica()
   		#self.#print Conf()
				



		

#inicio=clasifica()
#inicio.main("test0.txt", "PesosC0_4M0_4_500000.txt")		