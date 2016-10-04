from Tkinter import *

class Interface():
    def label(self, frame, label, col, line, justify = "left", colspan=1, linespan=1):
	return Label(frame, text = label).grid(row=line, column=col, columnspan = colspan, rowspan = linespan)

    def labelvar(self, frame, labelvar, col, line, justify = "left", colspan=1, linespan=1):
	s = StringVar()
	s.set(labelvar)
	return s, Label(frame, textvariable = s).grid(row=line, column=col, columnspan=colspan, rowspan=linespan)
    
    def button(self, frame, label, order, col, line, justify = "left", colspan=1, linespan=1):
	return Button(frame, text = label, command = order).grid(row=line, column=col, columnspan=colspan, rowspan=linespan)
    
    def entry(self, frame, col, line, justify = "left"):
	return Entry(frame).grid(row=line, column=col)