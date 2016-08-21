import sys, tty, termios

def getch():
    # workaround to simulate correct EOF-behavior when working on piped input
    char = sys.stdin.read(1)
    if char:
        return char
    else:
        return chr(4)

def puts(string):
    for char in string:
        putch(char)

def putch(char):
    sys.stdout.write(char)
    sys.stdout.flush()
