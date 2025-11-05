stack = []

stack.append('1')
stack.append('2')
stack.append('3')
print("Stack: ", stack)

element = stack.pop()
print("Pop: ", element)

topElement = stack[-1]
print("Peek:",topElement)

print("Size:",len(stack))