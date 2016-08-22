import sys
import brainfuck_utils as bu
from MemoryTape import MemoryTape

def main():
    
    ptr = 0
    ptr = bu.set_val(ptr, bu.EOF_REG, 4) # EOF character 0x04 is stored in R6

    # start the loop to read in a program until EOF
    ptr = bu.store_char(ptr, bu.INPUT_REG) # read in and store the next character in R5...
    ptr = bu.copy(ptr, bu.INPUT_REG, bu.CHAR_REG) # ... and also copy it to R13
    ptr = bu.sub(ptr, bu.INPUT_REG, bu.EOF_REG) # R5 = R5 - R6
    
    ptr = bu.while_loop_start(ptr, bu.INPUT_REG) # loop until EOF is received

    ptr = bu.write_char(ptr, bu.CHAR_REG)
    
    ptr = bu.store_char(ptr, bu.INPUT_REG) # get the next character...
    ptr = bu.copy(ptr, bu.INPUT_REG, bu.CHAR_REG) # and also copy it to R13
    ptr = bu.sub(ptr, bu.INPUT_REG, bu.EOF_REG) # R5 = R5 - R6
    ptr = bu.while_loop_end(ptr, bu.INPUT_REG) # complete the outer (EOF) loop

if __name__ == "__main__":
    main()
