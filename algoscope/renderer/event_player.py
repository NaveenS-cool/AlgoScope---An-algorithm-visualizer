from renderer.arrows import VisualPointer


class EventPlayer:
    def __init__(self, canvas, array_view, events, root):
        self.canvas = canvas
        self.array_view = array_view
        self.events = events
        self.root = root

        self.paused=False
        self.auto_play=True

        self.pointers = {}   # name -> VisualPointer
        self.current = 0     # event index

    def play(self):
        if self.current >= len(self.events):
            return  # done

        event = self.events[self.current]
        self.handle_event(event)

    def next(self, delay=400):
        self.current += 1

        if self.auto_play and not self.paused:
            self.canvas.after(delay, self.play)

    def pause(self):
        self.paused=True
    def resume(self):
        if self.paused:
            self.paused=False
            self.play()
    def step_forward(self):
        if self.current< len(self.events):
            self.play()

    def handle_event(self, event):
        etype = event["type"]

        if etype == "pointer_created":
            index = event["index"]
            name = event["name"]

            x = self.array_view.index_to_x(index)
            y = self.array_view.start_y

            self.pointers[name] = VisualPointer(self.canvas, name, x, y)
            self.next()

        elif etype == "pointer_moved":
            name = event["name"]
            index = event["index"]

            pointer = self.pointers[name]
            target_x = self.array_view.index_to_x(index)

            pointer.animate_to(target_x, self.next)

        elif etype == "swap":
            i = event["i"]
            j = event["j"]
            self.array_view.animate_swap(i, j, self.next)

        elif etype=="compare":
            i=event["i"]
            j=event["j"]

            self.array_view.animate_compare(i,j,self.next)

        else:
            self.next()


