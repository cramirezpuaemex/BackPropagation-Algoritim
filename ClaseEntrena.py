# Programa de redes neuronales basado en el codigo escrito en C++ de Roberto Alejo Eleuterio
#Desarrollado por Carlos Ramirez Pina
import random
import matplotlib.pyplot as plt
import copy
import tkFileDialog 
from tkFileDialog import askopenfilename
class ClaseEntrena():
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
			##print  i
		##print  elementos
		self.elementos1 = []
		for i in elementos:
			lista=i.split(",")
			lista.remove("\n")
		 	self.elementos1.append([(e) for e in lista])
		 	#lista1=lista.split("\n")
		 	#self.elementos1.append(lista)
		self.Q=len(self.elementos1)
		self.N=len(self.elementos1[0])
		self.X=[]
		##print  self.elementos1[0][0]
		##print  "Q", self.Q
		##print  "jjkhjkhjkhjk", len(self.elementos1[0])
		for i in range(self.Q):
			aux=[]
			for j in range(self.N-1):
				##print  "i", i,"j", j 
				aux.append(float(self.elementos1[i][j]))
			aux.append(1)#se le aumenta el bias
			aux.append(int(self.elementos1[i][-1]))# se le asigna la clase
			self.X.append((aux))
			
		self.N=self.N #Se le suma el bias
		self.NoClases()

	def NoClases(self):

		clases=self.X
		self.b=[]
		for i in clases:
			if len(self.b)==0:
				self.b.append(i[-1])
			else:
				if i[-1] not in self.b:
					self.b.append(i[-1])
					
		self.b.sort()
		#print  self.b
		self.J=len(self.b)
		self.ptrxcls=[0 for i in range(self.J)]
		for i in clases:
			pos=i[-1]
			##print  pos
			self.ptrxcls[pos]=self.ptrxcls[pos]+1




		#self. netNeural()

		##print  "numero de atributos", self.N, "no patrones", self.Q,"numero de clases o salidas", self.J, "numero de neuronas", self.M
		##print  "self.ptrxcls", self.ptrxcls
		#for i in self.X:
			#print  i
		#print  "numero de atributos", self.N, "no patrones", self.Q,"numero de clases o salidas", self.J, "numero de neuronas", self.M

		##print  self.X[1]
	def setUp(self):#Esta funcion manda llamar a todos los metodos de inicializacion
		self.initW()
		self.initU()
		self.initConf()


	def initW(self):
		self.W=[]
		self.Wa=[]
		#Aqui le modifique para que el vector de pesos W correspondieran con el numero de conexciones que debe de tener la red en este ejemplo que yohice es de 3x3
		for n in range(self.N):
			w = []
			wa=[]
			for m in range(self.M):#numero de neuronas de la capa oculta
				w.append((random.uniform(-0.5, 0.5)))
				wa.append(0)
			self.W.append(w)
			self.Wa.append(wa)

		#print  "tamanio de la matriz W", len(self.W), "x", len(self.W[0])
		#print  "matriz W"
		#for i in self.W:
			#print  i
		

	def initU(self):
		#Llena pesos de conexion de la capa oculta--------------------------------------------------------------------------------------------
		self.U = []
		self.Ua=[]
		for m in range(self.M+1):# se incluye el bias en la capa oculta
			u=[]
			ua=[]
			for j in range(self.J): # numero de neuronas en la capa de salida
				u.append((random.uniform(-0.5, 0.5)))
				ua.append(0)
			self.U.append(u)
			self.Ua.append(ua)

		#print  'tamano de la matriz U', len(self.U),"x", len(self.U[0])
		#print  "matriz U"

		#for i in self.U:
			#print  i
			
	def sigmoide(self, net):
		exp=(2.718281)
		resultado=((1)/(1+pow((exp),(-net))))
		return resultado
	#/***************************************************************************/
	#//Proceso de aprendizaje de la red
	def learning (self):
		for i in range(self.I):
		#for (int i=0;i<I;i++):
			for q in range(self.Q):
			#for(int q=0;q<Q;q++):
				self.forwardW(q) 
				self.update(q)
				
			self.getMse()	
			#self.#print Mse(i)
			if (self.mse < self.EMSGlobal):
				break
		
	#/*************************************************************************
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
		
	#/***************************************************************************/
	def desiredOutput(self, q):#{ //Determina la salida deseada de la muestra "q"
		self.t=[]
		for j in range(self.J):
		#for(int j=0;j<J;j++){
			if (self.X[q][-1]== j):
				self.t.append(0.9)
			else:
				self.t.append(0.1)
	#/***************************************************************************/
	def update(self, q):#{ //Actualiza los pesos de la red
		aux=0
		#for(int m=0;m<M+1;m++){ //mas 1 del bias ...
		for m in range(self.M+1): #mas 1 del bias ...
			#for(int j=0;j<J;j++){
			for j in range(self.J):
				#aux = self.eta*(self.t[j]-self.z[j])*(z[j]*(1-z[j])*y[m]);
				self.U[m][j] = self.U[m][j] + self.eta*((self.t[j]-self.z[j])*(self.z[j]*(1-self.z[j])*self.y[m]) + self.mu*(self.U[m][j]-self.Ua[m][j])) #// Se incluye el momento mu
				#U[m][j] = U[m][j] + eta*(T[q][j]-z[j])*(z[j]*(1-z[j])*y[m]);
			#for(int n=0;n<N;n++)
			for n in range(self.N):
				#for(int jj=0;jj<J;jj++){
				for jj in range(self.J):
					aux = (self.t[jj]-self.z[jj])*(self.z[jj]*(1-self.z[jj])*self.U[m][jj])
					#//W[n][m] = W[n][m] + eta*aux*(y[m]*(1-y[m]))*X[q][n];
					if m<self.M:
						self.W[n][m] = self.W[n][m] + self.eta*aux*(self.y[m]*(1-self.y[m]))*self.X[q][n] + self.mu*(self.W[n][m]-self.Wa[n][m])  # Se incluye el momemento mu
		self.valAnt()

	#/***************************************************************************/
	def valAnt(self): #//Guarda lo valores anteriores de los peos W y U.
		#self.Wa=copy.deepcopy(self.W)
		#self.Ua=copy.deepcopy(self.U)
		# #for(int m=0;m<M+1;m++)
		for m in range(self.M+1):
			#for(int j=0;j<J;j++)
			for j in range(self.J):
				self.Ua[m][j] = self.U[m][j]

		#for(int n=0;n<N;n++)
		for n in range(self.N):
			#for(int m=0;m<M+1;m++)
			for m in range(self.M):
				self.Wa[n][m] = self.W[n][m]
	
	#/***************************************************************************/
	def getMse(self):#{ //Obtine el erros cuadratico medio global, y por clase.
		#aux=0
		self.mse=0
		# #for(int j=0; j < J; j++)
		for j in range(self.J):
		 	self.msexcls.append(0)
  #       	#for(int q=0;q<Q;q++){
		for q in range(self.Q):
			aux=0
			self.forwardW(q)
			#for(int j=0;j<J;j++){
			for j in range(self.J):
				aux =aux+pow(self.t[j] - self.z[j],2)
			self.mse = self.mse+(aux/self.J)
			self.msexcls[self.X[q][self.N]] =self.msexcls[self.X[q][self.N]]+aux
			#for(int j=0; j < J ;j++)
		for j in range(self.J):
			self.msexcls[j] =self.msexcls[j] / self.ptrxcls[j]
		self.mse = self.mse /self.Q
		print  "error global", self.mse
		self.contErrores.append(self.mse)

	#/***************************************************************************/
	def initPtrXcls(self):
		self.ptrxcls=[]
		for j in range(self.J):
			self.ptrxcls[j].append(0)

	#/***************************************************************************/
	def printMse(self, i):#{ //Imprime el error cuadratico medio en la iteracion "i"
		#print  "Iter",i
		#for(int j=0; j < J ;j++)
		for j in range(self.J):
			print  self.msexcls[j]
		#//#print f(" mse: %f ptrmin: %d ptrmaj: %d maj/min: %f ",mse,ptrxcls[1],ptrxcls[0],msexcls[0]/msexcls[1]);
		##print f("\n");

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
				#print  self.z[j]
				Max =self.z[j]
				clss =j
		#print  "clss", clss
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
	
	#/***************************************************************************/
	def grafica(self):
		x=[]
		y=self.contErrores
		cont=0
		for i in range(len(y)):
			x.append(cont)
			cont=cont+1

		# Creamos una figura
		plt.figure()

		# Representamos
		plt.plot(x,y)
		#plt.plot(x,y)
		# Mostramos en pantalla
		plt.ylabel('error cuadratico medio')
		plt.xlabel('epocas')
		plt.show()
	# 	#print "pesos ultimos de  w", W, "\n"
	# 	#print "pesos mejores de w", PW, "\n"
	# 	#print "pesos ultimos del Bias", bias, "\n"
	# 	#print "pesos minimos del Bias", PB, "\n"
	# 	#print "pesos ultimo de U", U, "\n"
	# 	#print "pesos minimos de U", PU, "\n"
	# 	#print "pesos ultimos del Bias1", bias1, "\n"
	# 	#print "pesos minimos del Bias1", PB1, "\n"
	# 	#print "bias", pesosBias
	# 	#print  "bias1", pesosBias1
	# 	#print  "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	# 	###print  "El error minimo fue: ", minimo
	# 	#print  "En la iteracion: ", NIteracion
	def imprimirArchivo(self):
		aux1=[]
		aux2=[]

		

		for e in self.W:
	 		for j in e:
	 			aux1.append(j)
		for e in self.U:
	 		for j in e:
	 			aux2.append(j)
	 	fo = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt", title="Ingresa el nombre para el archivo de parametros libres Clas. Debe tener extension .txt") 			
		#fo = open('PesosEntrenarClasificacion.txt', 'w')
		##print >>fo,PW,'\n', PB, '\n', PU, '\n', PB1
		
		fo.write(str(self.M)+","+str(self.J)+",")
		fo.write("\n")
 		for i in aux1:
 			fo.write(str(i)+',')
 		fo.write("\n")

 		for e in aux2:
 			fo.write(str(e)+',')
 		fo.write("\n")

		
 		#print  ":)"
 		fo.close()
 	#*****************************************************************************
 	#*****************************************************************************
	def main(self, ruta, Fcorrecion, Moment,NNeuronas,NNIteraciones, errorMinimo):
		self.eta = Fcorrecion #Razon de aprendizaje o learning rate
		self.mu =Moment #Momento 
		self.N=0 #no. atributos 
		self.Q=0 #no. de patrones
		self.J=0 #no. de clases o salidas
		self.M=NNeuronas #no. de neuronas ocultas
		self.I=NNIteraciones #no. de iteraciones
		self.EMSGlobal=errorMinimo
		self.contErrores=[]
		self.msexcls=[]
		self.lecturaArchivo(ruta)
		self.setUp()
		self.learning()

		self.getAcc()
		self.imprimirArchivo()
		#self.muestraBarraestado()
		self.grafica()
		#self.#print Conf()



		

#inicio=ClaseEntrena()
#inicio.main("entreBase2.txt", 0.1, 0.3, 3, 5000, 0.0001)