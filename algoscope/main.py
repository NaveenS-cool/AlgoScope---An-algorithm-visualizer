from core.events import EventLogger
from core.visual_array import VisualArray
from core.pointers import Pointer
from renderer.event_player import EventPlayer
from renderer.array_view import VisualArrayView

import tkinter as tk

logger = EventLogger()

array = [3,1,2]

arr = VisualArray(array.copy(),logger)

i = Pointer("i",0,logger)

while i.get() < len(arr)-1:

    if arr.compare(i.get(),i.get()+1):
        arr.swap(i.get(),i.get()+1)
    i.move(i.get()+1)
    
events = logger.get_events()

for event in events:
    print(event)


root = tk.Tk()
root.title("AlgoScope")

canvas = tk.Canvas(root,width=800,height=400,bg="white")
canvas.pack()



box_height=40
box_width=60
start_x=50
start_y=150

arr_view = VisualArrayView(canvas,array,start_x,start_y,box_width,box_height)

player = EventPlayer(canvas,arr_view,events,root)

control_frame = tk.Frame(root)
control_frame.pack()

btn_play = tk.Button(control_frame,text="Play",command=player.resume)
btn_pause = tk.Button(control_frame,text="Pause",command=player.pause)
btn_step = tk.Button(control_frame,text="Step",command=player.step_forward)

btn_play.pack(side="left")
btn_pause.pack(side="left")
btn_step.pack(side="left")

player.play()

root.mainloop()