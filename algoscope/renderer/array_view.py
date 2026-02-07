
class VisualArrayView:
    def __init__(self,canvas,values,start_x,start_y,box_width=60,box_height=40):

        self.canvas=canvas
        self.values=values
        self.start_x = start_x
        self.start_y = start_y
        self.box_width = box_width
        self.box_height = box_height

        self.boxes=[]
        self.texts=[]

        self._draw_()

    def _draw_(self):

        for i,value in enumerate(self.values):

            x1 = self.start_x + i*self.box_width
            y1=self.start_y
            x2=x1+self.box_width
            y2= y1+self.box_height

            rect = self.canvas.create_rectangle(x1,y1,x2,y2)
            text = self.canvas.create_text(
                (x1+x2)/2,
                (y1+y2)/2,
                text = str(value),
                font = ("Arial",14)
            )

            self.boxes.append(rect)
            self.texts.append(text)




