from Tkinter import Tk
from tkFileDialog import askopenfilename
class OpenFile():
	filename = ""
	def pathfile(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		self.filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
		return(self.filename)
