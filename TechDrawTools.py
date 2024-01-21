import PySide                    #  PySide
from PySide import QtCore, QtGui #  PySide
from functools import partial

class LineAttributes:
    '''Operate all line attributes'''
    Colors = {'black':         ((0.0, 0.0, 0.0, 0.0),'000000'),\
                       'grey':          ((0.7, 0.7,0.7, 0.0),'b6b6b6'),\
                       'red':            ((1.0, 0.0, 0.0, 0.0),'ff0000'),\
                       'green':       ((0.0, 1.0, 0.0, 0.0),'00ff00'),\
                       'blue':          ((0.0, 0.0, 1.0, 0.0),'0000ff'),\
                        'magenta':((1.0, 0.0, 1.0, 0.0),'ff00ff'),\
                        'cyan':         ((0.0, 1.0, 1.0, 0.0),'00ffff')}
    Styles = {'solid': 1, 'dashed':2, 'dotted':3}
    Width = {'thick': 0.6, 'middle': 0.42, 'thin': 0.3}

    def __init__(self):
        self.LineColor =  self.Colors['black']
        self.LineStyle = self.Styles['dashed']
        self.LineWidth = self.Width['middle']

    def setColor(self,Color):
        self.LineColor = self.Colors[Color]

    def getColorTuple(self):
        return self.LineColor[0]

    def getColorHex(color):
        return LineAttributes.Colors[color][1]

    def setStyle(self,Style):
        self.LineStyle = self.Styles[Style]

    def getStyle(self):
        return self.LineStyle

    def setWidth(self,Width):
        self.LineWidth = self.Width[Width]

    def getWidth(self):
        return self.LineWidth

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        def radioButton(Box,Slot,Y,Tip,Text,Color='black',Checked = False):
            ''' create a radio button '''
            Button = QtGui.QRadioButton(Box)
            Button.setGeometry(QtCore.QRect(10, Y, 100, 20))
            if Checked:
                Button.setMouseTracking(True)
                Button.setChecked(True)
            Button.setText(Text)
            Button.setStyleSheet("color : #"+LineAttributes.getColorHex(Color)) 
            Button.setToolTip(Tip+Text)
            Button.clicked.connect(partial(Slot,Text))

        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("TechDraw Tools")
        MainWindow.resize(209, 410)
        MainWindow.setMaximumSize(QtCore.QSize(209, 410))
        self.centralWidget = QtGui.QWidget(MainWindow)

        ''' First Groupbox Commands -------------------------------------------------------------------'''
        self.groupBox_01 = QtGui.QGroupBox('Commands',self.centralWidget)
        self.groupBox_01.setGeometry(QtCore.QRect(10, 10, 191, 189))
        ''' Button: CircleCenterLines------------------------------------------------------------'''
        self.PB_CenterLines= QtGui.QPushButton(self.groupBox_01)
        self.PB_CenterLines.setGeometry(QtCore.QRect(10, 30, 172, 28))
        self.PB_CenterLines.setText("Draw circle centerLines")
        self.PB_CenterLines.setToolTip("Draw a center line cross at circles:"+ "\n"
                                                                       "- pick favoured line attributes"+ "\n"
                                                                       "- select many circles or arcs"+ "\n"
                                                                       "- click this button")
        self.PB_CenterLines.clicked.connect(self.on_PB_CircleCenterLines_clicked) # slot: "CircleCenterLines"
        ''' Button: DrawHoleCircle ------------------------------------------------------------'''
        self.PB_DrawHoleCircle= QtGui.QPushButton(self.groupBox_01)
        self.PB_DrawHoleCircle.setGeometry(QtCore.QRect(10, 60, 172, 28))
        self.PB_DrawHoleCircle.setText("Draw holecircle centerlines")
        self.PB_DrawHoleCircle.setToolTip("Draw the center lines of a hole circle:"+ "\n"
                                                                              "- pick favoured line attributes"+ "\n"
                                                                              "- select the circles of the hole circle"+ "\n"
                                                                              "- select a circle or arc beeing concentric to the hole circle"+ "\n"
                                                                              "- click this button")
        self.PB_DrawHoleCircle.clicked.connect(self.on_PB_DrawHoleCircle_clicked) # slot: "DrawHoleCircles"
        ''' Button: DrawCosmeticTread ------------------------------------------------------------'''
        self.PB_DrawCosmeticTread= QtGui.QPushButton(self.groupBox_01)
        self.PB_DrawCosmeticTread.setGeometry(QtCore.QRect(10, 90, 172, 28))
        self.PB_DrawCosmeticTread.setText("Draw cosmetic tread")
        self.PB_DrawCosmeticTread.setToolTip("Draw cosmetic threads:"+ "\n"
                                                                                       "- pick favoured line attributes"+ "\n"
                                                                                       "- select many circles"+ "\n"
                                                                                       "- click this button")
        self.PB_DrawCosmeticTread.clicked.connect(self.on_PB_DrawCosmeticTread_clicked) # slot: "DrawCosmeticTread"
        ''' Button: CreateIntersectionVertex ---------------------------------------------------'''
        self.PB_CreateIntersectionVertex= QtGui.QPushButton(self.groupBox_01)
        self.PB_CreateIntersectionVertex.setGeometry(QtCore.QRect(10, 120, 172, 28))
        self.PB_CreateIntersectionVertex.setText("Vertex at Intersection")
        self.PB_CreateIntersectionVertex.setToolTip("Create the vertexes at intersection of lines:"+ "\n"
                                                                                                 "- select two lines/circles/arcs"+ "\n"
                                                                                                 "- click this button")
        self.PB_CreateIntersectionVertex.clicked.connect(self.on_PB_IntersectionVertex_clicked) # slot: "CreateIntersectionVertex"
        ''' Button: ChangeLineStyle ------------------------------------------------------------'''
        self.PB_ChangeLineStyle= QtGui.QPushButton(self.groupBox_01)
        self.PB_ChangeLineStyle.setGeometry(QtCore.QRect(10, 150, 172, 28))
        self.PB_ChangeLineStyle.setText("Change the linestyle")
        self.PB_ChangeLineStyle.setToolTip("Change style/width/color of lines:"+ "\n"
                                                                                "- pick favoured line attributes"+ "\n"
                                                                                "- select many lines/circles/arcs"+ "\n"
                                                                                "- click this button")
        self.PB_ChangeLineStyle.clicked.connect(self.on_PB_ChangeLineStyle_clicked) # slot: "ChangeLineStyle"

        ''' Second Groupbox: radio Buttons for selecting the linestyle-------------------'''
        self.groupBox_02 = QtGui.QGroupBox('Line attributes',self.centralWidget) 
        self.groupBox_02.setGeometry(QtCore.QRect(10, 200, 95, 85))
        radioButton(self.groupBox_02,self.on_RB_ChangeStyle_Clicked,20,"set lines to ",'solid')
        radioButton(self.groupBox_02,self.on_RB_ChangeStyle_Clicked,40,"set lines to ",'dashed','black',True)
        radioButton(self.groupBox_02,self.on_RB_ChangeStyle_Clicked,60,"set lines to ",'dotted')

        ''' Third Groupbox:  radio Buttons for selecting the colors ------------------------'''
        self.groupBox_03 = QtGui.QGroupBox(self.centralWidget) 
        self.groupBox_03.setGeometry(QtCore.QRect(105, 200, 95, 160))
        radioButton(self.groupBox_03,self.on_RB_ChangeColor_Clicked,20,"set lines color to ",'black','black',True)
        radioButton(self.groupBox_03,self.on_RB_ChangeColor_Clicked,40,"set lines color to ",'grey','grey')
        radioButton(self.groupBox_03,self.on_RB_ChangeColor_Clicked,60,"set lines color to ",'red','red')
        radioButton(self.groupBox_03,self.on_RB_ChangeColor_Clicked,80,"set lines color to ",'green','green')
        radioButton(self.groupBox_03,self.on_RB_ChangeColor_Clicked,100,"set lines color to ",'blue','blue')
        radioButton(self.groupBox_03,self.on_RB_ChangeColor_Clicked,120,"set lines color to ",'magenta','magenta')
        radioButton(self.groupBox_03,self.on_RB_ChangeColor_Clicked,140,"set lines color to ",'cyan','cyan')

        ''' Fourth Groupbox radio Buttons for selecting the width -------------------------------'''
        self.groupBox_04 = QtGui.QGroupBox(self.centralWidget) 
        self.groupBox_04.setGeometry(QtCore.QRect(10, 275, 95, 85))
        radioButton(self.groupBox_04,self.on_RB_ChangeWidth_Clicked,20,"set lines width to ",'thick')
        radioButton(self.groupBox_04,self.on_RB_ChangeWidth_Clicked,40,"set lines width to ",'middle','black',True)
        radioButton(self.groupBox_04,self.on_RB_ChangeWidth_Clicked,60,"set lines width to ",'thin')

        ''' Button: Quit -------------------------------------------------------------------'''
        self.PB_Quit = QtGui.QPushButton(self.centralWidget)
        self.PB_Quit.setGeometry(QtCore.QRect(140, 370, 60, 28))
        self.PB_Quit.setText("Quit")
        self.PB_Quit.setToolTip("Quit TechDraw tools")
        self.PB_Quit.clicked.connect(self.on_PB_Quit_clicked) # slot: "quit"

        MainWindow.setCentralWidget(self.centralWidget)
        MainWindow.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_PB_CircleCenterLines_clicked(self): # slot: DrawCircleCenterLines
        '''
        Draw the center line cross at TechDraw circles
        '''
        Sel = Gui.Selection.getSelectionEx()[0]
        ObjectList = Sel.SubElementNames
        View = Gui.Selection.getCompleteSelection()[0]
        for ObjectString in ObjectList:
            if ObjectString[0:4] == 'Edge':
                Edge = View.getEdgeBySelection(ObjectString)
                if Edge.Curve.TypeId == 'Part::GeomCircle':
                    Object = Edge.Curve
                    Center = Object.Center
                    Radius = Object.Radius+2
                    Right = App.Vector(Center.x+Radius,Center.y,0)
                    Left = App.Vector(Center.x-Radius,Center.y,0)
                    Top = App.Vector(Center.x,Center.y+Radius,0)
                    Bottom = App.Vector(Center.x,Center.y-Radius,0)
                    Style, Width, Color = Attrib.getStyle(), Attrib.getWidth(), Attrib.getColorTuple()
                    View.makeCosmeticLine(Left,Right,Style, Width, Color)
                    View.makeCosmeticLine(Top,Bottom,Style, Width, Color)

    def on_PB_DrawHoleCircle_clicked(self): # slot: DrawHoleCircle
        '''
        Draw a center circle and center cross at a hole circle
        '''
        Sel = Gui.Selection.getSelectionEx()[0]
        ObjectList = [Obj for Obj in Sel.SubElementNames]
        View = Gui.Selection.getCompleteSelection()[0]
        if len(ObjectList) < 2: return
        Style, Width, Color = Attrib.getStyle(), Attrib.getWidth(), Attrib.getColorTuple()
        BigCircle = ObjectList.pop()
        if BigCircle[0:4] == 'Edge':
            BigEdge = View.getEdgeBySelection(BigCircle)
            if BigEdge.Curve.TypeId == 'Part::GeomCircle':
                BigObject = BigEdge.Curve
                BigCenter = BigObject.Center
        for ObjectString in ObjectList:
            if ObjectString[0:4] == 'Edge':
                Edge = View.getEdgeBySelection(ObjectString)
                if Edge.Curve.TypeId == 'Part::GeomCircle':
                    Object = Edge.Curve
                    Center = Object.Center
                    ObjRadius = Object.Radius
                    RadVec = Center.sub(BigCenter)
                    Radius = RadVec.Length
                    RadVec1 =RadVec.normalize()
                    StartDist = Radius-ObjRadius-2
                    EndDist = Radius+ObjRadius+2
                    EndPt = BigCenter+RadVec1.scale(EndDist,EndDist,EndDist)
                    RadVec1.normalize()
                    StartPt = BigCenter+RadVec1.scale(StartDist,StartDist,StartDist)
                    Tag = View.makeCosmeticLine(StartPt,EndPt,Style, Width, Color)
        BigRadius =Center.sub(BigCenter).Length
        View.makeCosmeticCircle(BigCenter, BigRadius, Style, Width, Color)

    def on_PB_DrawCosmeticTread_clicked(self): # slot: DrawCosmeticTread
        '''
        Draw a cosmetic thread at selected circles
        '''
        Sel = Gui.Selection.getSelectionEx()[0]
        ObjectList = Sel.SubElementNames
        View = Gui.Selection.getCompleteSelection()[0]
        for ObjectString in ObjectList:
            if ObjectString[0:4] == 'Edge':
                Edge = View.getEdgeBySelection(ObjectString)
                if Edge.Curve.TypeId == 'Part::GeomCircle':
                    Object = Edge.Curve
                    Center = Object.Center
                    Radius = Object.Radius/0.85
                    View.makeCosmeticCircleArc(Center, Radius, 255, 165, Attrib.getStyle(), Attrib.getWidth(), Attrib.getColorTuple())

    def on_PB_ChangeLineStyle_clicked(self): # slot: ChangeLineStyle
        '''
        Change style/ thickness/color of selected lines
        '''
        Sel = Gui.Selection.getSelectionEx()[0]
        ObjectList = Sel.SubElementNames
        View = Gui.Selection.getCompleteSelection()[0]
        for ObjectString in ObjectList:
            if ObjectString[0:4] == 'Edge':
                Edge = View.getCosmeticEdgeBySelection(ObjectString)
                oldFormat = Edge.Format
                newFormat = (Attrib.getStyle(),Attrib.getWidth(),Attrib.getColorTuple(),True)
                Edge.Format = newFormat
        View.requestPaint()

    def on_PB_IntersectionVertex_clicked(self): # slot: CreateIntersectionVertex
        '''
        Create  vertexes at intersection of two edges (lines and/or circles)
        '''
        Sel = Gui.Selection.getSelectionEx()[0]
        ObjectList = Sel.SubElementNames
        View = Gui.Selection.getCompleteSelection()[0]
        if len(ObjectList) < 2: return
        Edges = []
        for ObjectString in ObjectList:
            if ObjectString[0:4] == 'Edge':
                Edges.append(View.getEdgeBySelection(ObjectString))
        if Edges[0].Curve.TypeId == 'Part::GeomCircle':
            Line1 = Part.Circle(Edges[0].Curve.Center,App.Vector(0,0,1),Edges[0].Curve.Radius)
        else:
            Line1 = Part.Line(Edges[0].Vertexes[0].Point,Edges[0].Vertexes[1].Point)
        if Edges[1].Curve.TypeId == 'Part::GeomCircle':
            Line2 = Part.Circle(Edges[1].Curve.Center,App.Vector(0,0,1),Edges[1].Curve.Radius)
        else:
            Line2 = Part.Line(Edges[1].Vertexes[0].Point,Edges[1].Vertexes[1].Point)
        InterPnts = Line1.intersect(Line2)
        for Ip in InterPnts[:2]:
            View.makeCosmeticVertex(App.Vector(Ip.X,Ip.Y,Ip.Z))

    def on_RB_ChangeColor_Clicked(self,color): # slot for colors
        Attrib.setColor(color)

    def on_RB_ChangeStyle_Clicked(self,style): # slot for styles
        Attrib.setStyle(style)

    def on_RB_ChangeWidth_Clicked(self,width): # slot for width
        Attrib.setWidth(width)

    def on_PB_Quit_clicked(self): # slot "quit"
        App.Console.PrintMessage("End of TechDraw Tools" + "\n")
        self.window.close()

Attrib = LineAttributes()
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
