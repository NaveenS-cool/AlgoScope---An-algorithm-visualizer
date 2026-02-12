
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
    
    def index_to_x(self, index):
        return self.start_x + index * self.box_width + self.box_width / 2

    def animate_swap(self, i, j, on_done, steps=20, delay=20):
        text_i = self.texts[i]
        text_j = self.texts[j]

        xi, yi = self.canvas.coords(text_i)
        xj, yj = self.canvas.coords(text_j)

        dx_i = (xj - xi) / steps
        dx_j = (xi - xj) / steps

        def step(count=0):
            if count >= steps:
                self.texts[i], self.texts[j] = self.texts[j], self.texts[i]
                on_done()
                return
            self.canvas.move(text_i, dx_i, 0)
            self.canvas.move(text_j, dx_j, 0)
            self.canvas.after(delay, lambda: step(count + 1))

        step()





