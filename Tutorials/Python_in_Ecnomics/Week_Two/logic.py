
x = 1 #True
y = 0 #False 

x and y #0
x and x #1

not y #True
not x #False

x or y #1
y or y #0
x or x #1

def and_gate(x, y):
    if x and y:
        return 1
    else:
        return 0


def or_gate(x, y):
    if x or y:
        return 1
    else:
        return 0

def not_gate(x):
    if x:
        return not x
    else:
        return not not x

def xor_gate(x, y):
    if x == y:
        return 0
    else:
        return 1

#NOT
