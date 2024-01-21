# -*- coding: utf-8 -*-
# Macro Begin: C:\3D_CAD_LIBRARY\MACRO\adddensity.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
####		Every time click shortcut key, Material type can be added to the part files as a FeaturePython object
####		Material type is "Al", "Steel", "Plastic" can be switched each other by pressing shortcut key again and again
####		Recommand shortcut key setting : Ctrl + Shift + S

import FreeCAD
doc = App.ActiveDocument
viewObject = Gui.ActiveDocument

a = 0

for obj in FreeCAD.ActiveDocument.Objects:
	if obj.Label == "Al":
		a = 1 
	elif  obj.Label == "Steel":
		a = 2
	elif obj.Label == "Plastic":
		a = 3
	else:
		continue

if a==1:
	FreeCAD.ActiveDocument.removeObject("App__FeaturePython")
	obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
	obj.Label = "Steel"
elif a==2:
	FreeCAD.ActiveDocument.removeObject("App__FeaturePython")
	obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
	obj.Label = "Plastic"
elif a==3:
	FreeCAD.ActiveDocument.removeObject("App__FeaturePython")
	obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
	obj.Label = "Al"
else:
	obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
	obj.Label = "Steel"
