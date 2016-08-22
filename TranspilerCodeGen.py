import sys
import brainfuck_utils as bu
from MemoryTape import MemoryTape

def main():
    ptr = 0

    ptr = bu.set_val(ptr, bu.EOF_REG, 4) # EOF character 0x04 is stored in R6

    # R14 - R21 contain the character set of the language
    ptr = bu.set_val(ptr, 14, ord('+'))
    ptr = bu.set_val(ptr, 15, ord('-'))
    ptr = bu.set_val(ptr, 16, ord('>'))
    ptr = bu.set_val(ptr, 17, ord('<'))
    ptr = bu.set_val(ptr, 18, ord('.'))
    ptr = bu.set_val(ptr, 19, ord(','))
    ptr = bu.set_val(ptr, 20, ord('['))
    ptr = bu.set_val(ptr, 21, ord(']'))

    # R22 contains the indentation counter (necessary since we're generating Python code...)
    ptr = bu.set_val(ptr, bu.INDENT_COUNTER, 0)

    # R7 contains the tab character (important for formatting the output code)
    ptr = bu.set_val(ptr, bu.TAB_CHAR, ord('\t'))
    ptr = bu.set_val(ptr, bu.NEWLINE_CHAR, ord('\n'))

    # first write out the import statements to make the program run without further changes
    ptr = bu.write_string(ptr, 'from MemoryTape import MemoryTape\n')
    ptr = bu.write_string(ptr, 'import putget as pg\n')
    ptr = bu.write_string(ptr, 'ptr=0\n')
    ptr = bu.write_string(ptr, 'mem=MemoryTape()\n')

    # start the loop to read in a program until EOF
    ptr = bu.store_char(ptr, bu.INPUT_REG) # read in and store the next character in R5...
    ptr = bu.copy(ptr, bu.INPUT_REG, bu.CHAR_REG) # ... and also copy it to R13

    ptr = bu.sub(ptr, bu.INPUT_REG, bu.EOF_REG) # R5 = R5 - R6
    ptr = bu.while_loop_start(ptr, bu.INPUT_REG) # loop until EOF is received

    # do the command parsing here: use the copy in R13 and compare it to R14 - R21.
    # for each command, output the correct indentation and then the corresponding python equivalent

    # for "+"
    ptr = bu.if_not_equal(ptr, bu.CHAR_REG, 14)
    ptr = bu.if_else(ptr, bu.CHAR_REG)
    ptr = bu.write_indentation(ptr)
    ptr = bu.write_string(ptr, 'mem[ptr]+=1')
    ptr = bu.if_end(ptr, bu.CHAR_REG)

    # for "-"
    ptr = bu.if_not_equal(ptr, bu.CHAR_REG, 15)
    ptr = bu.if_else(ptr, bu.CHAR_REG)
    ptr = bu.write_indentation(ptr)
    ptr = bu.write_string(ptr, 'mem[ptr]-=1')
    ptr = bu.if_end(ptr, bu.CHAR_REG)

    # for ">"
    ptr = bu.if_not_equal(ptr, bu.CHAR_REG, 16)
    ptr = bu.if_else(ptr, bu.CHAR_REG)
    ptr = bu.write_indentation(ptr)
    ptr = bu.write_string(ptr, 'ptr+=1')
    ptr = bu.if_end(ptr, bu.CHAR_REG)

    # for "<"
    ptr = bu.if_not_equal(ptr, bu.CHAR_REG, 17)
    ptr = bu.if_else(ptr, bu.CHAR_REG)
    ptr = bu.write_indentation(ptr)
    ptr = bu.write_string(ptr, 'ptr-=1')
    ptr = bu.if_end(ptr, bu.CHAR_REG)

    # for "."
    ptr = bu.if_not_equal(ptr, bu.CHAR_REG, 18)
    ptr = bu.if_else(ptr, bu.CHAR_REG)
    ptr = bu.write_indentation(ptr)
    ptr = bu.write_string(ptr, 'pg.putch(chr(mem[ptr]))')
    ptr = bu.if_end(ptr, bu.CHAR_REG)

    # for ","
    ptr = bu.if_not_equal(ptr, bu.CHAR_REG, 19)
    ptr = bu.if_else(ptr, bu.CHAR_REG)
    ptr = bu.write_indentation(ptr)
    ptr = bu.write_string(ptr, 'mem[ptr]=ord(pg.getch())')
    ptr = bu.if_end(ptr, bu.CHAR_REG)

    # for "["
    ptr = bu.if_not_equal(ptr, bu.CHAR_REG, 20)
    ptr = bu.if_else(ptr, bu.CHAR_REG)
    ptr = bu.write_indentation(ptr)
    ptr = bu.write_string(ptr, 'while mem[ptr]:')
    ptr = bu.incr(ptr, bu.INDENT_COUNTER)
    ptr = bu.if_end(ptr, bu.CHAR_REG)

    # for "]"
    ptr = bu.if_not_equal(ptr, bu.CHAR_REG, 21)
    ptr = bu.if_else(ptr, bu.CHAR_REG)
    ptr = bu.decr(ptr, bu.INDENT_COUNTER)
    ptr = bu.if_end(ptr, bu.CHAR_REG)

    ptr = bu.write_newline(ptr)

    ptr = bu.store_char(ptr, bu.INPUT_REG) # get the next character...
    ptr = bu.copy(ptr, bu.INPUT_REG, bu.CHAR_REG) # and also copy it to R13
    ptr = bu.sub(ptr, bu.INPUT_REG, bu.EOF_REG) # R5 = R5 - R6
    ptr = bu.while_loop_end(ptr, bu.INPUT_REG) # complete the outer (EOF) loop

if __name__ == "__main__":
    main()
