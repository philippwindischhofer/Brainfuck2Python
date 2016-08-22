import putget as pg

# declarations of special-purpose memory cells reserved for specified functions:
PRINT_REG = 0 # used for preparation of characters to be printed
FOR_REG = 1 # used for FOR-loops
TEMP_REG_A = 2 # general-purpose register for temporary storage

# used for if-clauses
IF_REG_A = 3 
IF_REG_B = 4
IF_REG_C = 23
IF_REG_D = 24

EOF_REG = 6 # always holds the EOF-character
TAB_CHAR = 7 # stores the '\t' character
NEWLINE_CHAR = 8 # stores the '\n' character

# new characters are read into here...
INPUT_REG = 5
CHAR_REG = 13 # ... and copied to here

# stores the current indentation
INDENT_COUNTER = 22

def write_indentation(ptr):
    ptr = copy(ptr, INDENT_COUNTER, FOR_REG)
    ptr = for_loop_start(ptr, FOR_REG)
    ptr = write_char(ptr, TAB_CHAR)
    ptr = for_loop_end(ptr, FOR_REG)
    return ptr

# equivalent to if(op_a == op_b) {...}
def if_not_equal(ptr, op_a, op_b):
    ptr = copy(ptr, op_a, IF_REG_C)
    ptr = copy(ptr, op_b, IF_REG_D)
    ptr = sub(ptr, IF_REG_C, IF_REG_D)
    ptr = if_start(ptr, IF_REG_C)
    return ptr

#equivalent to if(op) {...} else {...}
def if_start(ptr, op):
    ptr = copy(ptr, op, IF_REG_A)
    ptr = copy(ptr, op, IF_REG_B)
    ptr = incr(ptr, IF_REG_A)
    ptr = set_ptr(ptr, IF_REG_B)
    pg.putch('[')
    return ptr

def if_else(ptr, op):
    ptr = reset(ptr, IF_REG_A)
    ptr = reset(ptr, IF_REG_B)
    pg.putch(']')
    ptr = set_ptr(ptr, IF_REG_A)
    pg.putch('[')
    return ptr

def if_end(ptr, op):
    ptr = reset(ptr, IF_REG_A)
    pg.putch(']')
    return ptr

# calculates op_a = op_a - op_b
def sub(ptr, op_a, op_b):
    ptr = reset(ptr, TEMP_REG_A)

    # start subtraction loop:
    ptr = for_loop_start(ptr, op_b)
    ptr = decr(ptr, op_a)
    ptr = incr(ptr, TEMP_REG_A)
    ptr = for_loop_end(ptr, op_b)

    # restore op_b to its original value
    ptr = for_loop_start(ptr, TEMP_REG_A)
    ptr = incr(ptr, op_b)
    ptr = for_loop_end(ptr, TEMP_REG_A)
    return ptr

# copies content of cell_source to cell_dest
def copy(ptr, cell_source, cell_dest):
    ptr = reset(ptr, TEMP_REG_A)
    ptr = reset(ptr, cell_dest)

    # start copy loop: carried out 'cell_source' times
    ptr = for_loop_start(ptr, cell_source)
    ptr = incr(ptr, cell_dest)
    ptr = incr(ptr, TEMP_REG_A)
    ptr = for_loop_end(ptr, cell_source)

    # restore cell_source to its original value
    ptr = for_loop_start(ptr, TEMP_REG_A)
    ptr = incr(ptr, cell_source)
    ptr = for_loop_end(ptr, TEMP_REG_A)
    return ptr

# equivalent to: while(cell)
def while_loop_start(ptr, cell):
    ptr = for_loop_start(ptr, cell)
    return ptr

# indicates the end of a while loop linked to cell
def while_loop_end(ptr, cell):
    ptr = set_ptr(ptr, cell)
    pg.putch(']')
    return ptr

# equivalent to: for(int ii = 0; ii < cell; ii++)
def for_loop_start(ptr, cell):
        ptr = set_ptr(ptr, cell)
        pg.putch('[')
        return ptr

# indicates the end of a for loop linked to cell 'cell'
def for_loop_end(ptr, cell):
        ptr = decr(ptr, cell)
        pg.putch(']')
        return ptr
        
# increments content of cell 'cell'
def incr(ptr, cell):
    ptr = set_ptr(ptr, cell)
    pg.putch('+')
    return ptr

# decrements content of cell 'cell'
def decr(ptr, cell):
    ptr = set_ptr(ptr, cell)
    pg.putch('-')
    return ptr
    
# reads in character from stdin and stores it at cell 'cell'
def store_char(ptr, cell):
    ptr = set_ptr(ptr, cell)
    pg.putch(',')
    return ptr

# writes out the string 'string'
def write_string(ptr, string):
    for char in string:
        ptr = set_val(ptr, PRINT_REG, ord(char))
        ptr = write_char(ptr, PRINT_REG)
    return ptr

def write_newline(ptr):
    ptr = write_char(ptr, NEWLINE_CHAR)
    return ptr

# prints the character contained in cell 'cell'
def write_char(ptr, cell):
    ptr = set_ptr(ptr, cell)
    pg.putch('.')
    return ptr

# sets the memory cell at 'cell' to 'val'
def set_val(ptr, cell, val):
    ptr = reset(ptr, cell) # first clear the cell to start from scratch
    repeat('+', val)
    return ptr

# clears the content of cell 'cell' (i.e. sets it to zero)
def reset(ptr, cell):
    ptr = set_ptr(ptr, cell)
    pg.puts('[-]')
    return ptr

# sets the pointer to an arbitrary (new) position
def set_ptr(ptr, new_ptr):
    if new_ptr >= ptr:
        repeat('>', new_ptr - ptr)
    else:
        repeat('<', ptr - new_ptr)
    return new_ptr

# 'unrolled' brainfuck loop
def repeat(char, iterations):
    for ii in range(iterations):
        pg.putch(char)
