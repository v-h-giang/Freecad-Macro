##	Author :		Vu Hoang Giang
##	Date:		2021 May 17
####		Reload file of SELECTED linked objects in Assembly document
####		Expand all sub-linked-assembly-type part in the Assembly to SELECT linked object 
####		Dont need care about selected thing is linked object or not, Can select all the list in assembly file
####		Recommand shortcut key setting : Ctrl + Shift + R

import sys

sys.path.append("C:\\Program Files\\FreeCAD 0.19\\bin")
sys.path.append("C:\\Program Files\\FreeCAD 0.19\\Mod")
sys.path.append("C:\\Program Files\\FreeCAD 0.19\\bin\Lib")

import FreeCAD
import newDatumCmd
import subprocess
import numpy as np
from PySide import QtCore, QtGui
import gc

Maindocname =  App.ActiveDocument.Name
FirstTab  =  Gui.getMainWindow().findChild(QtGui.QMdiArea).currentSubWindow().windowTitle()
doc = App.ActiveDocument
viewObject = Gui.ActiveDocument
Element = Gui.Selection.getSelection()

print("Begin Auto Reload Process")
s = len(Element)
ElementLinksources = []
i = 0
ActionNumber = 0

for i in range(s):
	if str(Element[i]) == "<App::Link object>":
		if ElementLinksources.count(Element[i].LinkedObject.Document.Name) != 0 :
			continue
		else:
			ActionNumber += 1
			ElementLinksources.append(Element[i].LinkedObject.Document.Name)
	else:
		ActionNumber += 1

s = len(ElementLinksources)

for i in range(s):
	try:
		App.setActiveDocument(ElementLinksources[i])
		ActionNumber += 1
		print("Begin Reload : ",App.ActiveDocument.Name)	
		App.ActiveDocument.restore()
		ActionNumber += 2
		print("Document :" ,ElementLinksources[i], "....... Imported")
		CurrentTab = Gui.getMainWindow().findChild(QtGui.QMdiArea).currentSubWindow().windowTitle()
		while  CurrentTab !=  FirstTab:
			print("Close tab", CurrentTab," of  file",  ElementLinksources[i])
			Gui.runCommand('Std_CloseActiveWindow')
			CurrentTab = Gui.getMainWindow().findChild(QtGui.QMdiArea).currentSubWindow().windowTitle()				
			ActionNumber += 2
		n = gc.collect()
		print("Memory Garbage Collection !!! ")
		print("Unreachable objects: ",n)
		print("Remaining Garbage: ", gc.garbage)
	except:
		print("EXCEPT event happened !!!! but we dont care :D ! ")

print("Request Completed")
print("Reloaded Files : ",  s)
print("省略された操作の数 :  ", ActionNumber)
print("節約できる時間 :  ", ActionNumber*2)
sys.path.remove("C:\\Program Files\\FreeCAD 0.19\\bin")
sys.path.remove("C:\\Program Files\\FreeCAD 0.19\\Mod")
sys.path.remove("C:\\Program Files\\FreeCAD 0.19\\bin\Lib")
doc.recompute()
