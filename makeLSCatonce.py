# Macro Begin: C:\3D_CAD_LIBRARY\MACRO\makeLCS.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
##	Author :		Vu Hoang Giang
##	Date:		2021 May 16
##	Recommend : Set shortcut key for this macro to Ctrl + Shift + A
##	this macro make LCS for  all SELECTED hole edges
##	Can use to making LCS for any edge 
##	remember to toggle document first 

import sys
sys.path.append("C:\Program Files\FreeCAD 0.19\bin")
sys.path.append("C:\Program Files\FreeCAD 0.19\Mod")
sys.path.append("C:\Program Files\FreeCAD 0.19\bin")
sys.path.append("C:\Program Files\FreeCAD 0.19\bin\Lib")

import FreeCAD
import newDatumCmd
import subprocess

doc = App.ActiveDocument
viewObject = Gui.ActiveDocument
active_body = Gui.ActiveDocument.ActiveView.getActiveObject('pdbody')
Element = Gui.Selection.getSelection()[0].Name
SubElement = Gui.Selection.getSelectionEx()[0].SubElementNames
print(Element)
print(SubElement)
s = len(SubElement)
print(s)
i = 0
for i in range(s):
	obj1 = active_body.newObject('PartDesign::CoordinateSystem','LCS_sc')
	obj1.Support = (doc.getObject(Element), [SubElement[i],])
	obj1.MapMode = 'Concentric'
	obj1.recompute()

print( str(i+1) +  " LCSs is created")
