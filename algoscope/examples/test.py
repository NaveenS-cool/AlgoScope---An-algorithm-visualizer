from core.events import EventLogger
from core.visual_array import VisualArray
from core.pointers import Pointer

logger = EventLogger()
arr = VisualArray([3,1,2],logger)

i=Pointer("i",0,logger)

while i.get() < len(arr)-1:
    if arr.compare(i.get(),i.get()+1):
        arr.swap(i.get(),i.get()+1)

    i.move(i.get()+1)

print("Final array",arr.rawdata())

print("\n Events:")

for e in logger.get_events():
    print(e)