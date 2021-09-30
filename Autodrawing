import FreeCAD, Part, Drawing
import PartDesignGui
from datetime import date
Maindocname =  App.ActiveDocument.Name
try:
	Piece=Gui.Selection.getSelection()[0]
except:
	Piece=FreeCAD.ActiveDocument.Objects[0]

Gui.activateWorkbench("TechDrawWorkbench")
class page:
	def __init__(self,borderleft=40,borderunder=50,bordertop=170,boderrigh=267,spaceX=60,spaceY=45,drawscale=1):
		self.borderleft = borderleft
		self.borderunder = borderunder
		self.bordertop=bordertop
		self.boderrigh=boderrigh
		self.spaceX = spaceX
		self.spaceY = spaceY
		self.drawscale = drawscale
		self.pagematrix=[borderleft,borderunder,bordertop,boderrigh,spaceX,spaceY,drawscale]

box = Piece.Shape.BoundBox
Lm = box.XMin
LM = box.XMax
Pm = box.YMin
PM = box.YMax
Hm = box.ZMin
HM = box.ZMax
L3d = LM - Lm  
P3d = PM - Pm 
H3d = HM - Hm 

def  setpage(P3d,H3d,L3d): #page horizon, page vertical, 
	p = P3d #Gui Object Oy size
	h = H3d #Gui Object Oz size	
	l = L3d  #Gui Object Ox size
	return p,h,l

A4 = page()
BL,BH,DH,DL,sX,sY,drawscale=A4.pagematrix

for i in range(3):
	A4 = page()
	BL,BH,DH,DL,sX,sY,drawscale=A4.pagematrix
	if i == 0:
		P,H,L = setpage(P3d,H3d,L3d)
		vector1 = FreeCAD.Vector(1,0,0)
		vector2 = FreeCAD.Vector(0,1,0)
		Number = '000'
	elif i == 1:
		P,H,L = setpage(L3d,H3d,P3d)
		vector1 = FreeCAD.Vector(0,1,0)
		vector2 = FreeCAD.Vector(1,0,0)
		Number = '001'
	else:
		P,H,L = setpage(L3d,P3d,H3d)
		vector1 = FreeCAD.Vector(0,0,1)
		vector2 = FreeCAD.Vector(1,0,0)
		Number = '002'

	OX = P/2 + BL
	OY = H/2 + BH  
	OX1 = OX + P/2 + sX + L 
	OY1 = OY + H/2 + sY + L 
	if (OX1 >= DL and OY1 <= DH) or (((OX1-DL) >= (OY1-DH)) and  OX1 >= DL and OY1 >= DH):	
		drawscale = (DL-BL-sX)/(P+L)
		P = drawscale*P
		H = drawscale*H
		L = drawscale*L
		OX = P/2 + BL 
		OY = H/2 + BH 
		OX1 = OX + P/2 + sX + L
		OY1 = OY + H/2 + sY + L 
		print("Case 0 : OX",OX,"OY",OY,"OX1",OX1,"OY1",OY1)
		print("Shorten Ox of Page") 
		print("Drawing Scale is changed to", drawscale)
		print(" ")
		if  OY1 >DH:
			drawscale = (DH-BL-sY-6)/(H+L)*drawscale
			P = drawscale*P
			H = drawscale*H
			L = drawscale*L	
			OX = P/2 + BL 
			OY = H/2 + BH 
			OX1 = OX + P/2 + sX + L
			OY1 = OY + H/2 + sY + L 
			print("Case 0-1 : OX",OX,"OY",OY,"OX1",OX1,"OY1",OY1)
			print("And , Shorten Oy of Page ") 
			print("Next, Drawing Scale is changed to", drawscale)
			print(" ")
	elif  (OX1 < DL and OY1 > DH)  or  (((OX1-DL) < (OY1-DH)) and  OX1 >= DL and OY1 >= DH):
		drawscale = (DH-BL-sY-6)/(H+L)		
		P = drawscale*P
		H = drawscale*H
		L = drawscale*L	
		OX = P/2 + BL 
		OY = H/2 + BH 
		OX1 = OX + P/2 + sX + L
		OY1 = OY + H/2 + sY + L 
		print("Case 1 : OX",OX,"OY",OY,"OX1",OX1,"OY1",OY1)
		print("Shorten Oy of Page") 
		print("Drawing Scale is changed to", drawscale)
		print(" ")
		if  OX1 > DL:
			drawscale = (DL-BL-sX)/(P+L)*drawscale
			P = drawscale*P
			H = drawscale*H
			L = drawscale*L
			OX = P/2 + BL 
			OY = H/2 + BH 
			OX1 = OX + P/2 + sX + L
			OY1 = OY + H/2 + sY + L 
			print("Case 1 -1  : OX",OX,"OY",OY,"OX1",OX1,"OY1",OY1)
			print("And, Shorten Ox of Page") 
			print("Next,Drawing Scale is changed to", drawscale)
			print(" ")
	else: 
		drawscale = 1.0	 	
	
	drawpage = App.activeDocument().addObject('TechDraw::DrawPage','Page'+Number)
	drawpage = App.activeDocument().getObject('Page'+Number)
	tmp = App.activeDocument().addObject('TechDraw::DrawSVGTemplate', 'Template' + Number)
	tmp.Template = 'C:/Program Files/FreeCAD 0.19/data/Mod/TechDraw/Templates/A4_yamato_format.svg'
	drawpage.Template = tmp
	projectitem = App.activeDocument().addObject('TechDraw::DrawProjGroup','ProjGroup'+Number)
	projectitem = App.activeDocument().getObject('ProjGroup'+Number)
	drawpage.addView(projectitem)
	projectitem.addProjection('Front')
	projectitem.Source = Piece
	projectitem.ProjectionType = u"Third Angle"
	projectitem.Anchor.Direction = vector1
	projectitem.Anchor.RotationVector = vector2
	projectitem.Anchor.XDirection = vector2
	projectitem.X = OX
	projectitem.Y = OY
	if i ==1:
		sX= sX-25
		sY =sY-35
	projectitem.spacingX = sX
	projectitem.spacingY = sY
	projectitem.Scale = drawscale
	projectitem.Anchor.recompute()
	App.ActiveDocument.recompute()
	projectitem.addProjection('Right')
	projectitem.addProjection('Top')
	ddview = App.activeDocument().addObject('TechDraw::DrawViewPart','View' + Number)
	ddview = App.activeDocument().getObject('View'+Number)
	drawpage.addView(ddview)
	ddview.Source = Piece
	ddview.Direction = FreeCAD.Vector(1.0,-1.0,1.0)
	ddview.XDirection = FreeCAD.Vector(1.0,1.0,1.0)
	ddview.X = DL - 20 
	ddview.Y = DH - 10
	ddview.Scale = drawscale
	App.activeDocument().recompute()
	Gui.ActiveDocument.resetEdit()
	


	texts = drawpage.Template.EditableTexts
	for key, value in texts.items():
	    print("{0} = {1}".format(key, value))
	texts["UNIT"] = Maindocname[0:5]
	texts["CAD FILE NAME"] = Maindocname
	texts["FC-scale"] = '{:.1f}'.format(drawscale)
	texts["PART NAME"] = Maindocname
	texts["FC-DATE"] = date.today().strftime("%b-%d-%Y")
	texts["NAME2"] = '丸山'
	for obj in FreeCAD.ActiveDocument.Objects:
		if obj.Label == "Al":
			texts["FC-MAT"]  = "アルミ"
			texts["SHORI"] = "黒アルマイト"
		elif  obj.Label == "Steel":
			texts["FC-MAT"]  = "SUS304"
		elif obj.Label == "Plastic":
			texts["FC-MAT"]  = "PVC"
		else:
			continue
	drawpage.Template.EditableTexts = texts
