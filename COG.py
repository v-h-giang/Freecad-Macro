##	Author :		Vu Hoang Giang
##	Date:		2021 May 17
##		Calculate Center of Gravity on Choosen Parts in Assemblied Tree 
####		You must choose Link:Parts in Assembly File first and run this macro
####		Default density is steel with all choosen parts 
####  	Material of parts can be added to the part files by 'going to linked objects' (S,G), and run under command:
####			obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
####			obj.Label = "Steel"  ## or "Plastic" "Al" 
####		Recommend : use "addDensity.FCMacro" with short cut key (ctrl + shift + S ) to adding Marterial type to parts
####		Recommand shortcut key setting : Ctrl + Shift + B


import sys
sys.path.append("C:\Program Files\FreeCAD 0.19\bin")
sys.path.append("C:\Program Files\FreeCAD 0.19\Mod")
sys.path.append("C:\Program Files\FreeCAD 0.19\bin")
sys.path.append("C:\Program Files\FreeCAD 0.19\bin\Lib")

import FreeCAD
import newDatumCmd
import subprocess
import numpy as np

Maindocname =  App.ActiveDocument.Name
doc = App.ActiveDocument
viewObject = Gui.ActiveDocument
Element = Gui.Selection.getSelection()


DensityFe=7.9 # Fe
DensityAl=2.7 # Al
DensityPlastic=1.4 #PVC plastic
DensityDefault = DensityFe

s = len(Element)
ElementName = []
ElementCenter = []
ElementVolume = []
ElementMaterial = []
ElementLinksources =[]
ElementDensity = []
Cal1 = []
Cal2 =[]
i = 0

try:
	for i in range(s):
		ElementLinksources.append(Element[i].LinkedObject.Document.Name)
		ElementName.append(Element[i].Name)
		ElementCenter.append(doc.getObject(ElementName[i]).Shape.CenterOfMass)
		ElementVolume.append(doc.getObject(ElementName[i]).Shape.Volume)
	print("All checked parts will be check:" +str(ElementLinksources))
	for i in range(s):
		App.setActiveDocument(ElementLinksources[i])
		print("Searching Document :" + ElementLinksources[i])
		a = 0
		for objinfile in FreeCAD.ActiveDocument.Objects:
			if objinfile.Label == "Al":
				a = 1
			elif  objinfile.Label == "Steel":
				a = 2
			elif objinfile.Label == "Plastic":
				a = 3
			else:	
				continue
		if a==1:
			ElementDensity.append(DensityAl)
		elif a==2:
			ElementDensity.append(DensityFe)
		elif a==3:
			ElementDensity.append(DensityPlastic)
		else:
			ElementDensity.append(DensityFe)
except:
	ElementCenter.append( doc.getObject(Element[0].Name).Shape.CenterOfMass)
	ElementVolume.append(doc.getObject(Element[0].Name).Shape.Volume)
	a = 0
	for objinfile in FreeCAD.ActiveDocument.Objects:
		if objinfile.Label == "Al":
			a = 1
		elif  objinfile.Label == "Steel":
			a = 2
		elif objinfile.Label == "Plastic":
			a = 3
		else:	
			continue
	if a==1:
		ElementDensity.append(DensityAl)
	elif a==2:
		ElementDensity.append(DensityFe)
	elif a==3:
		ElementDensity.append(DensityPlastic)
	else:
		ElementDensity.append(DensityFe)

App.setActiveDocument(Maindocname)
print("Element Name : " , ElementName)
print("Element Center :" , ElementCenter)
print("Element Volume" , ElementVolume)
print("Element Density" , ElementDensity)

for num1, num2,num3 in zip(ElementCenter, ElementVolume,ElementDensity):
	Cal1.append(num1*num2*num3)
	Cal2.append(num2*num3)

Mass = np.sum(Cal2)
center = np.sum(Cal1,axis=0)/Mass

print("Center of Gravity :" , center)
print("Mass :", Mass/10**6, "Kg")
CenterPlacement = FreeCAD.Placement()
CenterPlacement.Base = center

GroupDoc = doc.addObject('App::DocumentObjectGroup',  'CoG')
sphere = doc.addObject('Part::Sphere', 'CenterOfMass')
sphere.Placement = CenterPlacement
sphere.Radius = 5
sphere.ViewObject.ShapeColor = (0.6, 0.0, 0.0)
sphere.ViewObject.Transparency = 5
sphere.ViewObject.LineWidth = 1.0
GroupDoc.addObject(sphere)

### PlaneYZ
plan = doc.addObject('Part::Plane', 'PlaneYZ')
plan.Length = 100
plan.Width = 100
plan.Placement =  CenterPlacement
plan.Placement.Rotation = plan.Placement.Rotation.multiply(FreeCAD.Rotation(0.0, -90.0, 0.0))
plan.Placement.Base.x = center[0]
plan.Placement.Base.y = center[1]-50
plan.Placement.Base.z = center[2]-50

plan.ViewObject.LineColor = (1.0, 0.66667, 0.0)
plan.ViewObject.ShapeColor = (0.6, 0.0, 0.0)
plan.ViewObject.Transparency = 90
plan.ViewObject.LineWidth = 1.0
GroupDoc.addObject(plan)
### PlaneXZ
plan = FreeCAD.ActiveDocument.addObject('Part::Plane', 'PlaneXZ')
plan.Length = 100
plan.Width = 100

plan.Placement = CenterPlacement
plan.Placement.Rotation = plan.Placement.Rotation.multiply(FreeCAD.Rotation(0.0, 0.0, 90.0))
plan.Placement.Base.x = center[0]-50
plan.Placement.Base.y = center[1]
plan.Placement.Base.z = center[2]-50

plan.ViewObject.LineColor = (1.0, 0.66667, 0.0)
plan.ViewObject.ShapeColor = (0.0, 0.6, 0.0)
plan.ViewObject.Transparency = 90
plan.ViewObject.LineWidth = 1.0
GroupDoc.addObject(plan)

### PlaneXY
plan = FreeCAD.ActiveDocument.addObject('Part::Plane', 'PlaneXY')
plan.Length = 100
plan.Width = 100

plan.Placement = CenterPlacement
plan.Placement.Base.x = center[0]-50
plan.Placement.Base.y = center[1]-50
plan.Placement.Base.z = center[2]

plan.ViewObject.LineColor = (1.0, 0.66667, 0.0)
plan.ViewObject.ShapeColor = (0.0, 0.6, 0.0)
plan.ViewObject.Transparency = 90
plan.ViewObject.LineWidth = 1.0
GroupDoc.addObject(plan)

doc.recompute()
sys.path.remove("C:\Program Files\FreeCAD 0.19\bin")
sys.path.remove("C:\Program Files\FreeCAD 0.19\Mod")
sys.path.remove("C:\Program Files\FreeCAD 0.19\bin")
sys.path.remove("C:\Program Files\FreeCAD 0.19\bin\Lib")
