from Tkinter import *

# Christian Jose Soler: Estructura de Datos
# Grupo F: Lunes
# Practica 4: Tkinter y Colas

# Class that helps in the creation of widgets in the application
class Interface():
    def label(self, frame, label, col, line, justify = "left", colspan=1, linespan=1): 
    # Label creator
	return Label(frame, text = label).grid(row=line, column=col, columnspan = colspan, rowspan = linespan)

    def labelvar(self, frame, labelvar, col, line, justify = "left", colspan=1, linespan=1): 
    # Label with textvariable creator
	s = StringVar()
	s.set(labelvar)
	return s, Label(frame, textvariable = s).grid(row=line, column=col, columnspan=colspan, rowspan=linespan)
    
    def button(self, frame, label, order, col, line, justify = "left", colspan=1, linespan=1):
    # Button creator
	return Button(frame, text = label, command = order).grid(row=line, column=col, columnspan=colspan, rowspan=linespan)
    
    def entry(self, frame, col, line):
    # Entry creator
	entry = Entry(frame)
	entry.grid(row=line, column=col)
	return entry