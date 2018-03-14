'''
>>> import os
>>> os.getcwd()
'/home/user'
>>> os.chdir("/tmp/")
>>> os.getcwd()
'/tmp'


os.system('cls') # clear screen
'''

# Learn Tkinter

from Tkinter import *
from ttk import *
from PIL import Image

def part_1():
	import Tkinter
#import _tkinter
	Tkinter._test()


def hellosimple():
	root = Tk() # in Tkinter module; it's the parent
	## create Tk widgets: Button and Label
	button = Button(root, text = 'Click me') # Button in ttk module
	button.pack()
	button['text']
	button['text'] = 'Press me' # change text
	button.config(text = 'Push me') # change text
	button.config() # show arguments
	str(button) # underlying name
	str(root) # underlying name 
	Label(root, text = 'Hello, Tkinter!').pack() # create a label without storing the object to a variable

# more complex version of Hello, Tkinter!:
class HelloApp:
	def __init__(self, master):
		self.label = Label(master, text = "Hello, Tkinter!")
		self.label.grid(row = 0, column = 0, columnspan = 2)

		Button(master, text = 'Texas', \
			command = self.texas_hello).grid(row = 1, column = 0)
		Button(master, text = 'Hawaii', \
			command = self.Hawaii_hello).grid(row = 1, column = 1)
	def texas_hello(self):
		self.label.config(text = "Howdy, Tkinter!")
	def Hawaii_hello(self):
		self.label.config(text = "Aloha, Tkinter!")

def main():
	root = Tk()
	app = HelloApp(root)
	root.mainloop()
if __name__ == '__main__': main()

# Display text and image with labels:
root = Tk()
label = ttk.Label(root, text = "Hello, Tkinter!")
label.pack()
label.config(text = "Howdy, Tkinter!")
label.config(text = "Howdy, Tkinter! It\'s been a while since we\
	last met.")
label.config(wraplength = 150) # set width to avoid too long line.
label.config(justify = CENTER) # font in center
label.config(foreground = "blue", background = 'yellow') # set color
label.config(font = ("Courier", 18, 'bold'))
label.config(text = "Howdy, Tkinter!")
PhotoImage(file = "C:\\Users\\Zhixiong Cheng\\Desktop\\oshima-yuko-wallpaper-61693789.jpg")
logo = PhotoImage(file = "C:\\Users\\Zhixiong Cheng\
	\\Desktop\\oshima-yuko-wallpaper-61693789.jpg") # save it
label.config(image = logo)
label.config(compound = "text") # the compound option specifies the position of the image relative to the text.
label.config(compound = "center") # show both with text in center
label.config(compound = "left") # text to left
label.img = logo # save it inside this object
label.config(image = label.img) # can only read GIF and PGM/PPM

# capturing input with buttons:
root = Tk()
button = Button(root, text = "Click Me!")
button.pack()
def callback():
	print 'Clicked!'
button.config(command = callback) # function executed when clicked
button.invoke() # simulate the result without clicking
button.state(['disabled'])
button.instate(['disabled'])
button.state('!disabled')
button.instate(['!disabled'])
logo = PhotoImage(file = '')
button.config(image = logo, compound = LEFT)
small_logo = logo.subsample(5, 5) # resize image by every 5 pixel in x and y direction
button.config(image = small_logo)

'''
Tkinter Variable class:
BooleanVar, DoubleVar, IntVar, StringVar
'''
# Presenting choices with checkbuttons and radiobuttons:
root = Tk()
checkbutton = Checkbutton(root, text = 'SPAM?')
checkbutton.pack()
spam = StringVar()
spam.set('SPAM!')
spam.get()
checkbutton.config(variable = spam, onvalue = 'SPAM Please!'\
	, offvalue = 'Boo SPAM') # if no on/offvalue, it will be 1 when selected and 0 when unselected; and SPAM! when no actions
spam.get() # click checkbutton
spam.get() # unchoose checkbutton
## create another chocie: breakfast:
breakfast = StringVar()
Radiobutton(root, text = 'SPAM', variable = breakfast, \
	value = 'SPAM').pack()
Radiobutton(root, text = 'Eggs', variable = breakfast, \
	value = 'Eggs').pack()
Radiobutton(root, text = 'Sausage', variable = breakfast, \
	value = 'Sausage').pack()
Radiobutton(root, text = 'SPAM', variable = breakfast, \
	value = 'SPAM').pack()
breakfast.get() # select one of them, then check
checkbutton.config(textvariable = breakfast) # whataever you choose in radiobutton, it will show on text of check button.

# make one-line entry text: ttk.Entry:
root = Tk()
entry = Entry(root, width = 30)
entry.pack()
entry.get() # get user's input
entry.delete(0, 1) # delete range(0, 1)'s strings
entry.delete(0, END) # delete everything
entry.insert(0, 'Enter your password') # auto show text when no input
entry.config(show = '*') # hide user's input
entry.config(show = '') # make it back
entry.get() # get invisiable user's input
entry.state(['disabled']) # being grey
entry.state(['!disabled']) # can input again
entry.state(['readonly']) # can only select but not change

# makeing selection with combo box and spin box: 
root = Tk()
month = StringVar()
combobox = Combobox(root, textvariable = month)
combobox.pack()
combobox.config(value = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'))
month.get()
month.set('Dec') # can be set to the value not in Tuple
month.set('Not a month')
month.get() # can get types that whatever users type
year = StringVar()
Spinbox.config(root, textvariable = year, from_ = 1990, to = 2014).pack()
year.get()
year.get() # can get whatever user's input

# display status with Scale adn Progressbar: ttk.Scale/ ttk.Progressbar
root = Tk()
progressbar = Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()
progressbar.config(mode = 'indeterminate') # it will move forever
progressbar.start()
progressbar.stop()
progressbar.condig(mode = 'determinate', maximun = 11.0, value = 4.2)
progressbar.config(value = 8.0)
progressbar.step() # the default is 1.0
progressbar.step(5) # it will exceed 100%
value - DoubleVar()
progressbar.config(variable = value) # control the bar by Scale
scale = Scale(root, orient = HORIZONTAL, length = 400, variable = value, \
	from_ = 0.0, to = 11.0).pack()
scale.set(4.2) # can be set manually
scale.get()

# Organizing widgets with frames: ttk.Frame/ ttk.LabelFrame
## types of Frames:relief = FLAT, RAISED, SUNKEN, SOLID, RIDGE, GROOVE
root = Tk()
frame = Frame(root)
frame.pack()
frame.config(height = 100, width = 200)
frame.config(relief = RIDGE)
Button(frame, text = 'Click Me').grid() # button based on frame
frame.config(padding = (30, 15))
LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

# Creating additional top-level windows: Tkinter.Toplevel()
root = Tk()
window = Toplevel(root) # create a child window
window.title('New Window')
window.lower() # make it lower layer
window.lift(root) # make it high than root
window.state('zoomed') # make it full screen
window.state('withdrawn') # make is dispear
window.state('iconic') # make it minized
window.state('normal') # back to first state - zoomed
window.state()
window.state('normal')
window.iconify()
window.deiconify()
window.geometry('640*480+50+100')
window.resizable(False, False) # cannot be resize manually
window.maxsize(640, 480) # set max size to resize
window.minsize(200, 200) # set min size to resize
window.resizable(True, True) # make it can be resize again
root.destroy() # delete this window and all its children

# Seperating widgets within paned windows: ttk.Panedwindow
root = Tk()
panedwindow = Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill = BOTH, expand = True) # expand to fill the entire space inside of the top-level window; and want it to expand if that window is change in size.
frame1 = Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
panedwindow.add(frame1, weight = 1) # change of size when resizing
panedwindow.add(frame2, weight = 4) # add new widgets horizontally (on the right)
frame3 = Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)
panedwindow.insert(1, frame3) # insert it at any position
panedwindow.forget(1)

# grouping widget within a tabbed notebook:
root = Tk()
notebook = Notebook(root)
notebook.pack()
frame1 = Frame(notebook)
frame2 = Frame(notebook)
notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two')
Button(frame1, text = 'Click Me!').pack() # add a button belong to first frame
frame3 = Frame(notebook)
notebook.insert(1, frame3, text = 'Three')
notebook.forget(1) # temporary forget index = 1
notebook.add(frame3, text = 'Three')
notebook.select() # get ID of which tab is currently selected by user
notebook.index(notebook.select()) # convert this ID to index number
notebook.select(2) # switch to select that tab with index 2
notebook.tab(1, state = 'disabled')
notebook.tab(1, state = 'hidden')
notebook.tab(1, state = 'normal')
notebook.tab(1, 'text') # get text of tab index 1
notebook.tab(1) # get all properties of tab index 1

# Entering and displaying multiple lines with Text widget: Tk.Text()
url = 'http://www.tkdocs.com/tutorial/text.html'
from Tkinter import *
root = Tk()
text = Text(root, width = 40, height = 10)
text.pack()
text.config(wrap = 'word') # could be char, word and none
text.get('1.0', 'end')
text.get('1.0', '1.end')
text.insert('1.0 + 2 lines', 'inserted message') # add in 4th row
text.insert('1.0 + 2 lines lineend', 'and\nmore and\nmore...')
text.delete('1.0')
text.delete('1.0', '1.0 lineend')
text.delete('1.0', '3.0 lineend + 1 chars')
text.replace('1.0', '1.0 lineend', 'This is the first line.')
text.config(state = 'disabled')
text.delete('1.0', 'end')
text.config(state = 'normal')

text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background = 'yellow')
rext.tag_remove('my_tag', '1.1', '1.3')
text.tag_range('my_tag')
text.tag_names()
text.tag_names('1.0')
text.replace('my_tag.first', 'my_tag.last', 'That')
text.tag_delete('my_tag')
text.mark_names()
text.insert('insert', '_')
text.mark_set('my_mark', 'end')
text.mark_gravity('my_mark', 'right')
text.mark_unset('my_mark')
image = PhotoImage(file  = 'C:\Users\Zhixiong Cheng\Desktop\download.gif')
text.image_create('insert', image = image)
button = Button(text, text = 'Click Me!')
text.window_create('insert', window = button)

# buildin a hirarchical treeview: ttk.Treeview()
root = Tk()
treeview = Treeview(root)
treeview.pack()
treeview.insert('', '0', 'item1', text = 'First Item')
treeview.insert('', '1', 'item2', text = 'Second Item')
treeview.insert('', 'end', 'item3', text = 'Third Item')
logo = PhotoImage(file = 'C:\Users\Zhixiong Cheng\Desktop\download.gif').subsample(10, 10)
treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)
treeview.config(height = 5)
treeview.move('item2', 'item1', 'end')
treeview.item('item1', open = True)
treeview.item('item1', 'open') # bool check
treeview.detach('item3') # temporary unshow
treeview.move('item3', 'item2', '0')
treeview.delete('item3')
## adding columns and selecting items in treeview
treeview.config(columns = ('version'))
treeview.column('version', width = 50, anchor = 'center')
treeview.column('#0', width = 150)
treeview.heading('version', text = 'Version')
treeview.set('python', 'version', '3.4.1')
treeview.item('python', tags = ('software'))
treeview.tag_configue('software', background = 'yellow')
def callback(event):
	print treeview.selection()
treeview.bind('<<TreeviewSelect>>', callback)
treeview.config(selectmode = 'browse') # select one at most
treeview.config(selectmode = 'none') # unable to select
treeview.selection_add('python')
treeview.selection_remove('python')
treeview.selection_toggle('python')

# Building cascading menus: its not ttk widgets, 
from Tkinter import *
root = Tk()
root.option_add('*tearOff', False) # remove dashed line from menu GUI
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')
from __future__ import print_function # in python 2, print is a statement, in 3, it's a funtion
file.add_command(label = 'New', command = lambda:print('new file'))
file.add_separator()
file.add_command(label = 'Open...', command = lambda:print('Opening file...'))
file.add_command(label = 'Save', command = lambda:print('Save...'))
## add accelerator and photos asides them
file.entryconfig('New', accelerator = 'Ctrl + N')
logo = PhotoImage(file = 'C:\Users\Zhixiong Cheng\Desktop\download.gif').subsample(10, 10)
file.entryconfig('Open...', image = logo, compound = 'left')
file.entryconfig('Open...', state = 'disabled')
file.delete('Save')
## create a cascade save and its sub-menus
save = Menu(file)
file.add_cascade(menu = save, label = 'Save')
save.add_command(label = 'Save As', command = lambda:print('Saving As...'))
save.add_command(label = 'Save All', command = lambda:print('Saving All...'))
## add radio buttons
choice = IntVar()
edit.add_radiobutton(label = 'One', variable = choice, value = 1)
edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
edit.add_radiobutton(label = 'Three', variable = choice, value = 3)
file.post(300, 400) # show up the content of file on position (300, 400) 

# Drawing a basic line by Canvas: Tkinter.Canvas()
from Tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack()
canvas.config(width = 640, height = 480)
line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5) # it has 2 points coords
canvas.itemconfigure(line, fill = 'green')
canvas.coords(line) # get coords
canvas.coords(line, 0, 0, 320, 240, 640, 0)
canvas.itemconfigure(line, smooth = True)
canvas.itemconfigure(line, splinesteps = 5)
canvas.itemconfigure(line, splinesteps = 100)
canvas.delete(line)
## Drawing complex shaps: rectangles, ovals, arcs and polygons
rect = canvas.create_rectangle(160, 120, 480, 360)
canvas.itemconfigure(rect, fill = 'yellow')
oval = canvas.create_oval(160, 120, 480, 360) # this is the coords of the rect around that oval
arc = canvas.create_arc(160, 1, 480, 240) # by default its 90 degree
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
poly = canvas.create_poly(160, 360, 320, 480, 480, 360, fill = 'blue')
text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))
logo = PhotoImage(file = 'C:\Users\Zhixiong Cheng\Desktop\download.gif')
image = canvas.create_image(320, 240, image = logo)
canvas.lift(text)
canvas.lower(image)
canvas.lower(image, text) # always keep the image just one layer lower than text
button = Button(canvas, text = 'Click Me')
canvas.create_window(320, 60, window = button)
## by granting items with tage, we can adjust properties of items with same tag at the same time
canvas.itemconfigure(rect, tag = ('shape'))
canvas.itemconfigure(oval, tag = ('shape', 'round'))
canvas.itemconfigure('shape', fill = 'grey')
canvas.gettags(oval)

# Attaching scroll bars to widgets: ttk.Scrollbar()
## create a scroll bar for Text:
from Tkinter import *
from ttk import *
root = Tk()
text = Text(root, width = 40, height = 10, wrap = 'word')
text.grid(row = 0, column = 0)
scrollbar = Scrollbar(root, orient = VERTICAL, command = text.yview)
scrollbar.grid(row = 0, column = 1, sticky = 'ns')
text.config(yscrollcommand = scrollbar.set)
## create a scroll bar for Canvas:
root = Tk()
canvas = Canvas(root, scrollregion = (0, 0, 640, 480), bg = 'white')
xscroll = Scrollbar(root, orient = HORIZONTAL, command = canvas.xview)
yscroll = Scrollbar(root, orient = VERTICAL, command = canvas.yview)
canvas.config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

canvas.grid(row = 1, column = 0)
xscroll.grid(row = 2, column = 0, sticky = 'ew')
yscroll.grid(row = 1, column = 1, sticky = 'ns')

def canvas_click(event):
	x = canvas.canvasx(event.x)
	y = canvas.canvasy(event.y)
	canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

canvas.bind('<1>', canvas_click)

root.mainloops() # this is to run in .py file

# Configuring widgets styles: ttk.Style()
root = Tk()
button1 = Button(root, text = 'Button 1')
button2 = Button(root, text = 'Button 2')
button1.pack()
button2.pack()
style = Style()
style.theme_names() # all themes avaliable for choose
style.theme_use() # currently use theme
style.theme_use('classic') # change a theme
style.theme_use('vista')
button1.winfo_class() # default style for button1 widgets
style.configure('TButton', fg = 'blue') # change TButton's style
style.configure('Alarm.TButton', foreground = 'orange', font\
	= ('Arial, 24', 'bold')) # create a new style
button2.config(style = 'Alarm.TButton')
style.map('Alarm.TButton', foreground = [('pressed', 'pink'),\
	('disabled', 'grey')])
button2.state(['disabled'])
style.layout('TButton') # all possible styles for TButton
style.element_options('Button.label')
style.lookup('TButton', 'foreground') # check current style

# Promoting users with Messagebox and dialogs: Tkinter.messagebox()
from Tkinter import messagebox
messagebox.showinfo(title = 'A Friendly Message', message = 'Hello, Tkinter!')
## Messagebox Types: Informational -- showinfo(), showwarning(), showerror()
messagebox.askyesno(title = 'Hungry?', message = 'Do you wanna SPAM?')
## Messagebox Types: Questions -- askyesno(), askokcancel(), askretrycancel(), askyesnocancel(), askquestion()
from Tkinter import filedialog
filename = filedialog.askopenfile() # save filename user selected to filename
filename.name # show name with path
## Filedialog Types: askopenfile(mode), askopenfiles(mode), askopenfilename(), askopenfilenames()
from Tkinter import colorchooser
colorchooser.askcolor(initialcolor = '#FFFFFF') # it will return the color user chose

# Geometry Management: Pack Geometry Manager
## Use when a widget is expended to fill its entire parent; Use to stack multiple widgets HORIZONTALLY or VERTICALLY
## Limited for complex layout
root = Tk()
Label(root, text = 'Hello! Tkinter!', background = 'yellow').pack() # it will stick on top and center of window and cannot resize when expanding windows
Label(root, text = 'Hello! Tkinter!', backgroung = 'yellow').pack(fill = X) # it will fill the x direction when stcreching out the X directions
Label(root, text = 'Hello! Tkinter!', background = 'yellow').pack(fill = BOTH, expand = True) # it will expand to both directions
label = Label(root, text = 'Hello!', background = 'yellow')
label.pack(side = LEFT, anchor = 'nw') # it will be packed HOROZANTALLY from LEFT TO RIGHT and stay and NW when straching the window
Label(root, text = 'Hello!', background = 'blue').pack(side = LEFT, padx = 10, pady = 10) # leave a room of 10 px on both direction
Label(root, text = 'Hello!', background = 'blue').pack(side = LEFT, ipadx = 10, ipady = 10) # expend the area of label by 10 px on both direction

for widget in root.pack_slaves():
	widget.pack_configure(fill = BOTH, expend = TRUE) # it will be applied to all widgets at the same time
	print widget.pack_info() # print details

label.pack_forget() # the yellow widget has been forget instead of deleting

# Grid Geometry Manager:
## Easy to organize widgets in 2D
root = Tk()
Label(root, text = 'Yellow', background = 'yellow').grid(row = 1, column = 1)
Label(root, text = 'Blue', background = 'blue').grid(row = 1, column = 0)
Label(root, text = 'Green', background = 'green').grid(row = 0, column = 0)
Label(root, text = 'Orange', background = 'orange').grid(row = 0, column = 1)
## more complex arrangement: one label occupy two space:
root = Tk()
Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2)
Label(root, text = 'Blue', background = 'blue').grid(row = 1, column = 0, columnspan = 2)
Label(root, text = 'Green', background = 'green').grid(row = 0, column = 0)
Label(root, text = 'Orange', background = 'orange').grid(row = 0, column = 1)
## stick, padx, pady, ipadx, ipady
root = Tk()
Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2, stick = 'nsew')
Label(root, text = 'Blue', background = 'blue').grid(row = 1, column = 0, columnspan = 2, stick = 'nsew')
Label(root, text = 'Green', background = 'green').grid(row = 0, column = 0, padx = 10, pady = 10, stick = 'nsew')
Label(root, text = 'Orange', background = 'orange').grid(row = 0, column = 1, ipadx = 25, ipady = 25, stick = 'nsew')
## Other Grid methods: grid_slaves(), grid_configure(), grid_info(), grid_forget()
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.columnconfigure(2, weight = 1)

# Place Geometry Manager
## exact control of widget location and size; difficult to manager a large number of widgets
root = Tk()
root.geometry('640*480+200+200')
Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)
Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')
## Other Place methods: place_slaves(), place_configure(), place_info()

# Event Handling: Configuring command callbacks:
## callback is function will execute when button is clicked
## Widgets with Command Callbacks: Button, Checkbutton, Radiobutton, Spinbox, Scale, Scrollbar
from Tkinter import *
from ttk import *
root = Tk()
def callback(number):
	print(number)

Button(root, text = 'Click me: 1', command = lambda: callback(1)).pack()
Button(root, text = 'Click me: 2', command = lambda: callback(2)).pack()
Button(root, text = 'Click me: 3', command = lambda: callback(3)).pack()

# Binding to keyboard events:
## Some of Event types: ButtonPress, ButtonRelease, Enter, Leave, Motion, KeyPress, KeyRelease, Focusln
## others:
url = 'http://www.tkdocs.com/tutorial/canvas.html#bindings'
root = Tk()
def key_press(event):
	print 'type:{}'.format(event.type)
	print 'widget:{}'.format(event.widget)
	print 'char:{}'.format(event.char)
	print 'keysym:{}'.format(event.keysym)
	print 'keycode:{}'.format(event.keycode)
def shortcut(action):
	print action
root.bind('<KeyPress>', key_press)
root.bind('<Control-c>', lambda e: shortcut('copy'))
root.bind('<Control-v>', lambda e: shortcut('paste'))
''' Keyboard Events:
<Key>, <KeyPress>: User pressed any key
<KeyPress-Delete>: User Pressed Delete key
<KeyRelease-Right>: User released Right Arrow key
a, b, c, 1, 2, 3, ... <space>, <less>: User pressed a "printable" key
<Shift_L>, <Control_R>, <F5>, <Up>: User pressed a 'special' key
<Return>: User pressed the Enter key
<Control-Alt-Next>: User pressed Ctrl+Alt+Page Down keys.
'''

# Binding to mouse events:
root = Tk()
def mouse_press(event):
	global prev
	prev = event
	print 'type: {}'.format(event.type)
	print 'widget: {}'.format(event.widget)
	print 'num: {}'.format(event.num)
	print 'x: {}'.format(event.x)
	print 'y: {}'.format(event.y)
	print 'x_root: {}'.format(event.x_root)
	print 'y_root: {}'.format(event.y_root)
canvas = Canvas(root, width = 640, height = 480,\
	background = 'white')
canvas.pack()
def draw(event):
	global prev
	canvas.create_line(prev.x, prev.y, event.x, event.y\
		, width = 5)
	prev = event

canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)
''' Mouse Events: Click-Related
<Button>, <ButtonPress>: Any button was pressed
<Button-1>, <ButtonPress-1>, <1>: Button 1 was pressed
<ButtonRelease-1>: Button 1 was released
<Double-Button-1> or <Triple-Button-1>: Button 1 was double- or triple-clicked
<Enter>: Mouse entered widget area
<Leave>: Mouse left widget area
<Motion>: Mouse was moved
<B1-Motion>: Mouse was moved with Button 1 held down.
'''

# Binding to virtual events:
from __future__ import print_function
from Tkinter import *
from ttk import *
root = Tk()
entry = Entry(root)
entry.pack()
entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number'))

print(entry.event_info('<<OddNumber>>'))

entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

entry.event_delete('<<OddNumber>>')

# Binding to multiple events:
from __future__ import print_function
from Tkinter import *
from ttk import *
root = Tk()
label1 = Label(root, text = 'Label 1')
label2 = Label(root, text = 'Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> label')) # all mouse action on label 1
label1.bind('<1>', lambda e: print('<1> label'))
root.bind('<1>', lambda e: print('<1> Root')) # it will trigger 2 events for <1>

label.unbind('<1>')
label.unbind('<ButtonPress>')

root.bind_all('<Escape>', lambda e: print('Escape'))

# Building an Application:
from Tkinter import *
from ttk import *
import tkMessageBox

class Feedback:
	def __init__(self, master):

		master.title('Explore Califonia Feedback')
		master.resizable(False, False)
		master.configure(background = '#e1d8b9')

		self.style = Style()
		self.style.configure('TFrame', background = '#e1d8b9')
		self.style.configure('TButton', background = '#e1d8b9')
		self.style.configure('TLabel', background = '#e1d8b9')
		self.style.configure('Header.TLabel', background = '#e1d8b9', font = ('Arial', 11))

		self.frame_header = Frame(master)
		self.frame_header.pack()

		self.logo = PhotoImage(file = 'C:\Users\Zhixiong Cheng\Desktop\download.gif').subsample(10, 10)
		Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
		Label(self.frame_header, text = 'Thanks for Exploring!', style = 'Header.TLabel').grid(row = 0, column = 1)
		Label(self.frame_header, wraplength = 300,\
			text = ("We're glad you chose Explore California for your recent adventure. "
				"Please tell us what you thought about the 'Desert to See' tour. ")).grid(row = 1, column = 1)
		
		self.frame_content = Frame(master)
		self.frame_content.pack()

		Label(self.frame_content, text = 'Name: ').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
		Label(self.frame_content, text = 'Email: ').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
		Label(self.frame_content, text = 'Comments: ').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

		self.entry_name = Entry(self.frame_content, width = 24, font = ('Arial', 10))
		self.entry_email = Entry(self.frame_content, width = 24, font = ('Arial', 10))
		self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))

		self.entry_name.grid(row = 1, column = 0, padx = 5)
		self.entry_email.grid(row = 1, column = 1, padx = 5)
		self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

		Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, sticky = 'e')
		Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, sticky = 'w')

	def submit(self):
		print 'Name: {}'.format(self.entry_name.get())
		print 'Email: {}'.format(self.entry_email.get())
		print 'Comments: {}'.format(self.text_comments.get(1.0, 'end'))
		self.clear
		tkMessageBox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')

	def clear(self):
		self.entry_name.delete(0, 'end')
		self.entry_email.delete(0, 'end')
		self.text_comments.delete(1.0, 'end')

def main():
	root = Tk()
	feedback = Feedback(root)
	root.mainloop()

if __name__ == '__main__': main()



