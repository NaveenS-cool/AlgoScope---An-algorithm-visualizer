import tkinter as tk
from arrows import VisualPointer
from array_view import VisualArrayView


root = tk.Tk()

root.title("AlgoScope")

canvas = tk.Canvas(root,width=800,height=400,bg="white")
canvas.pack()

box_height=40
box_width=60
start_x=50
start_y=150

values = [3,1,2]

arr_view = VisualArrayView(canvas,values,start_x,start_y,box_width,box_height)

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