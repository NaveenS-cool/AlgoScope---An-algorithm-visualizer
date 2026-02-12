import tkinter as tk
from arrows import VisualPointer
from array_view import VisualArrayView
from event_player import EventPlayer


root = tk.Tk()

root.title("AlgoScope")

canvas = tk.Canvas(root,width=800,height=400,bg="white")
canvas.pack()

box_height=40
box_width=60
start_x=50
start_y=150

events = [
    {"type": "pointer_created", "name": "i", "index": 0},
    {"type": "pointer_created", "name": "j", "index": 1},
    {"type": "pointer_moved", "name": "j", "index": 2},
    {"type": "swap", "i": 0, "j": 1}
]


values = [3,1,2]

arr_view = VisualArrayView(canvas,values,start_x,start_y,box_width,box_height)

player = EventPlayer(canvas, arr_view, events,root)
player.play()


root.mainloop()