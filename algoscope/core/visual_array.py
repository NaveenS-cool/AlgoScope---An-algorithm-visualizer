from core.events import EventLogger

class VisualArray:
    def __init__(self,data,logger:EventLogger):
        self.data=list(data)
        self.logger = logger

    def __len__(self):
        return len(self.data)

    def get_item(self,index):
        self.logger.log("read",index=index)
        return self.data[index]

    def set_item(self,index,value):
        self.logger.log("write",index=index,value=value)
        self.data[index]=value

    def compare(self,i,j):
        self.logger.log("compare",i=i,j=j)
        return (self.data[i]>self.data[j])

    def swap(self,i,j):
        self.logger.log("swap",i=i,j=j)
        self.data[i],self.data[j] = self.data[j],self.data[i]


    def rawdata(self):
        """For debugging"""
        return self.data