import sys
import putget as pg
from MemoryTape import MemoryTape

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
            mem[ptr] = ord(pg.getch())
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

if __name__ == "__main__":
    main(sys.argv[1:])
