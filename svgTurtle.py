import turtle
class svgTurtle(turtle.Turtle):
    def __init__(self, params):
        self.instructions = params
        super().__init__()
        super().pd()
    
    #debug       
    def drawCoords(self, turtleWriter):
        print("writing from",turtleWriter)
        turtleWriter.setposition(0,0)
        coordText=str(super().xcor())
        coordText+=" "
        coordText+=str(super().ycor())
        turtleWriter.write(coordText, font=('Arial',15,'bold'), align='left')
        
    def svg_M(self, x, y):     # 'M' key: moveTo
        print("M call:",x,",",y)
        super().pd()
        super().pu()
        super().setposition(x,y)

    def svg_l(self, dx, dy):    #'l' key: draw line to
        super().pd()
        super().setposition(dx,dy)
        super().pu()
        
    def render(self, debug):               #start drawing from commandlist
        for instruction in self.instructions:
            self.drawCoords(debug)
            switch={
                'M':self.svg_M(instruction[1][0], instruction[1][1]),
                'l':self.svg_l(instruction[1][0], instruction[1][1])
                }
            switch.get(instruction[0],"Invalid")
            print(instruction[0],"completed")


