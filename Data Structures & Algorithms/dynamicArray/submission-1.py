class DynamicArray:
    arr = []

    size = 0
    # update size when set item to the array
    # always count size everytime getsize is called
    def __init__(self, capacity: int):
        self.arr = []
        for i in range(capacity):
            self.arr.append(None)

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if self.arr[i] == None:
            self.size += 1
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # // check arr is full
        # // if yes, append and update size
        if(len(self.arr) == self.size):
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # // return and remove from array
        # // get the last item index
        # // access the last item from the index that we got 
        # // save to variable while removing, and then return it 
        lastIdx = self.getSize() - 1
        result = self.arr[lastIdx]
        self.arr[lastIdx] = None
        self.size -= 1
        return result

    def resize(self) -> None:
        # // append
        for i in range(len(self.arr)):
            self.arr.append(None)
        
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.arr)
