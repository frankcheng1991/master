from __future__ import division
from Tkinter import *

def iCalc(source, side): # return a Frame
	storeObj = Frame(source, borderwidth = 4, bd = 4, bg = "powder blue")
	storeObj.pack(side = side, expand = YES, fill = BOTH)
	return storeObj

def button(source, side, text, command = None): # return a Button
	storeObj = Button(source, text = text, command = command)
	storeObj.pack(side = side, expand = YES, fill = BOTH)
	return storeObj
class app(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.option_add('*Font', 'arial 20 bold') # # fonts for all widgets
		self.pack(expand = YES, fill = BOTH)
		self.master.title('Calculator') # Frame doesn't have title, root has

		display = StringVar()
		Entry(self, relief = RIDGE,
			textvariable = display, justify = 'right', bd = 30, bg = "powder blue").pack(side = TOP, expand = YES)


if __name__ == '__main__':
	root = Tk()
	App = app(root)
	root.mainloop() 