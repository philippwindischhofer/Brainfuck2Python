# Brainfuck2Python
This is a self-hosting Brainfuck-to-Python Transpiler (Source-to-Source compiler).

More information about the project can be found at <https://am241.wordpress.com/2016/08/22/a-strange-loop-each-day-keeps-boredom-away/>

Noteworthy contents:
```
./Interpreter.py        ... Brainfuck interpreter used to bootstrap the Transpiler
./CatCodeGen.py         ... Code generator implementing 'cat' in Brainfuck
./TranspilerCodeGen.py  ... Code generator implementing the Transpiler in Brainfuck
```

First, generate the Brainfuck sourcecode of the Tranpiler:
```
$ python2 TranspilerCodeGen.py > b2p.bf
```

To bootstrap the Transpiler, apply it to its own sourcecode by feeding it through the interpreter:
```
$ ((python2 Interpreter.py b2p.bf) < b2p.bf) > b2p.py
```

Then, translate any Brainfuck program back to Python:
```
$ python2 CatCodeGen.py > cat.bf
$ (python2 b2p.py < cat.bf) > cat.py
$ python2 cat.py < testinput.dat
This is 'cat' written in Brainfuck.
```
