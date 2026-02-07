import tkinter as tk
from arrows import VisualPointer


root = tk.Tk()

root.title("AlgoScope")

canvas = tk.Canvas(root,width=800,height=400,bg="white")
canvas.pack()

box_height=40
box_width=60
start_x=50
start_y=150

values = [3,1,2]

for i,value in enumerate(values):

    x1 = start_x + i*box_width
    y1=start_y
    x2=x1+box_width
    y2= y1+box_height

    canvas.create_rectangle(x1,y1,x2,y2)
    canvas.create_text(
        (x1+x2)/2,
        (y1+y2)/2,
        text = str(value),
        font = ("Arial",14)
    )
arrow_x = start_x + box_width + box_width/2

pointer = VisualPointer(canvas,"target",arrow_x,start_y)


def move_arrow_to(target_index,steps=20,delay=20):

    current_coords = canvas.coords(pointer.arrow)
    current_x = current_coords[0]

    target_x = start_x + target_index*box_width + box_width/2
    dx = (target_x - current_x)/steps

    def step(count=0):
        if count >= steps:
            pointer.move_to(target_x,start_y)
            return
        pointer.move(dx,0)
        root.after(delay,lambda:step(count+1))

    step()

move_arrow_to(2)


root.mainloop()