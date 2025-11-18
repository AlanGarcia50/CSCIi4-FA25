def evaluate_expression(x, y, o):
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
            return x / y
x=5
y=5
o="+"

x=1
y= -1
o="+"

x=0
y=-1
o="-"

x=0
y=5
o="/"

x=4
y=2
o="/"

x=2
y=1
o="*"

x=3
y=2
o="*"
print(evaluate_expression(x, y, o))