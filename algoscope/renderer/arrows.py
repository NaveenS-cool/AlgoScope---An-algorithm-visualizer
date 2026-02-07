

class VisualPointer:

    def __init__(self,canvas,name,x,y):
        self.canvas=canvas
        self.name=name
        self.arrow = canvas.create_line(
            x,y-40,
            x,y,
            arrow="last",
            width=2
        )
        self.label=canvas.create_text(
            x,y-50,
            text=name,
            font=("Arial",12)
        )

    def move(self,dx,dy=0):
        self.canvas.move(self.arrow,dx,dy)
        self.canvas.move(self.label,dx,dy)

    def move_to(self,x,y):
        self.canvas.coords(self.arrow,x,y-40,x,y)
        self.canvas.coords(self.label,x,y-50)