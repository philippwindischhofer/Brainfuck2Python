# implements the full memory tape, using two dynamic lists to implement the right / left infinite pieces
class MemoryTape:
    
    # automatically enlarging list used to implement the infinite memory tape
    class GrowingList(list):
        def __setitem__(self, index, value):
            if value < 0:
                value += 256
            if value > 255:
                value -= 256
            if index >= len(self):
                self.extend([0]*(index + 1 - len(self)))
            list.__setitem__(self, index, value)
                
    right = GrowingList()
    left = GrowingList()

    # keeps track of the maximum positions that have been written to the right / left
    max_right = 0
    max_left = 0

    def __init__(self):
        self.__setitem__(0, 0)

    def __getitem__(self, index):
        if index >= 0:
            if index > self.max_right:
                return 0
            else:
                return self.right[index]
        else:
            index = abs(index)
            if index > self.max_left:
                return 0
            else:
                return self.left[index]

    def __setitem__(self, index, value):
        if index >= 0:
            self.right[index] = value
            if index > self.max_right:
                self.max_right = index
        else:
            index = abs(index)
            self.left[index] = value
            if index > self.max_left:
                self.max_left = index

