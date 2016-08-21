import sys
import putget as pg

def main(argv):
    # first, get name of brainfuck source file to be interpreted (passed as the FIRST parameter)
    file = argv[0]

    # read in the code
    with open(file, 'r') as sourcefile:
        source = sourcefile.read()

    # build the tape and set pointer to its starting location
    mem = MemoryTape()
    ptr = 0
    
    # parse input program character by character and thus run the brainfuck program
    pos = 0
    while pos < len(source):
        char = source[pos] # get current command
        
        if char == '>':
            ptr += 1
            pos += 1
        elif char == '<':
            ptr -= 1
            pos += 1
        elif char == '+':
            mem[ptr] += 1
            pos += 1
        elif char == '-':
            mem[ptr] -= 1
            pos += 1
        elif char == '.':
            pg.putch(chr(mem[ptr]))
            pos += 1
        elif char == ',':
            mem[ptr] = pg.getch()
            pos += 1
        elif char == '[':
            if mem[ptr] == 0:
                # '[' counts +1, ']' counts -1
                balance = 1
                while balance != 0:
                    pos += 1
                    if source[pos] == '[':
                        balance += 1
                    elif source[pos] == ']':
                        balance -= 1
            pos += 1
        elif char == ']':
            if mem[ptr] != 0:
                balance = -1
                while balance != 0:
                    pos -= 1
                    if source[pos] == '[':
                        balance += 1
                    elif source[pos] == ']':
                        balance -= 1
            else:
                pos += 1

# implements the full memory tape, using two dynamic lists to implement the right / left infinite pieces
class MemoryTape:
    
    # automatically enlarging list used to implement the infinite memory tape
    class GrowingList(list):
        def __setitem__(self, index, value):
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

if __name__ == "__main__":
    main(sys.argv[1:])
