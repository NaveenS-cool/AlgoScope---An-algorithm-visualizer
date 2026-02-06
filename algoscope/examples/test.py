from core.events import EventLogger
from core.visual_array import VisualArray

logger = EventLogger()
arr = VisualArray([3,1,2],logger)

for i in range(len(arr)-1):
    if arr.compare(i,i+1):
        arr.swap(i,i+1)

print("Final array",arr.rawdata())

print("\n Events:")

for e in logger.get_events():
    print(e)