

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

    def animate_to(self, target_x, on_done, steps=20, delay=20):
        current_coords = self.canvas.coords(self.arrow)
        current_x = current_coords[0]
        current_y = current_coords[3]  # bottom of arrow

        dx = (target_x - current_x) / steps

        def step(count=0):
            if count >= steps:
                self.move_to(target_x, current_y)
                print("Animation finished — calling on_done")
                on_done()
                return
            self.move(dx, 0)
            self.canvas.after(delay, lambda: step(count + 1))

        step()
