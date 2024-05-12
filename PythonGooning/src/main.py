from collections import OrderedDict

class obj:
    def __init__(self, count):
        self.count = count
        self.array = []
        self.setup()
    def setup(self):
        for x in self.count:
            print(x)
            self.array[x] = x
    def print(self):
        for x in self.array:
            print(x)
   
object = obj(10)         
object.print()

