from z3 import *
x = BitVec('x', 32)
y = BitVec('y', 32)
z = BitVec('z', 32)
s = Solver()


def add_constraints(temp):
    for i in range(0,32,4):
        s.add(Or(Extract(i+3,i,temp) == 0x0,
          Extract(i+3,i,temp) == 0x1,
          Extract(i+3,i,temp) == 0x2,
          Extract(i+3,i,temp) == 0x3,
          Extract(i+3,i,temp) == 0x4,
          Extract(i+3,i,temp) == 0x5,
          Extract(i+3,i,temp) == 0x6,
          Extract(i+3,i,temp) == 0x7,
          Extract(i+3,i,temp) == 0x8,
          Extract(i+3,i,temp) == 0x9,
          Extract(i+3,i,temp) == 0xA,
          Extract(i+3,i,temp) == 0xB,
          Extract(i+3,i,temp) == 0xC,
          Extract(i+3,i,temp) == 0xD,
          Extract(i+3,i,temp) == 0xE,
          Extract(i+3,i,temp) == 0xF))

add_constraints(x)
add_constraints(y)
add_constraints(z)
s.add((x+z+y) * 2 + y  - 1 == 0)
s.add((y + x*2 + z ) * 2 + z - 1 == 0)
s.add((x+z+y) * 8 + x - z - y - y - 1 == 0 )
print(s.check())
print(hex(int(s.model()[x].as_string(),10))[2:])
print(hex(int(s.model()[y].as_string(),10))[2:])
print(hex(int(s.model()[z].as_string(),10))[2:])
