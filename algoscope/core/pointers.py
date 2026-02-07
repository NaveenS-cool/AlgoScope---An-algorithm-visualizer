from core.events import EventLogger

class Pointer:

    def __init__(self,name,index,logger:EventLogger):
        self.name=name
        self.index=index
        self.logger = logger

        self.logger.log("pointer_created",name=name,index=index)

    def move(self,new_index):
        self.index=new_index;
        self.logger.log("pointer_moved",name=self.name,index=self.index)


    def get(self):
        return self.index

    

    