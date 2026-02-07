import tkinter as tk


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
arrow_x = start_x + box_width/2

canvas.create_line(
    arrow_x,
    start_y-40,
    arrow_x,
    start_y,
    arrow=tk.LAST,
    width=2
)

canvas.create_text(
    arrow_x,
    start_y-50,
    text="pointer1",
    font=("Arial",12)
)

root.mainloop()