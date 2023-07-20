exp = "[3*(a+b)]*{a*c}{[(c+d)*(x/y)](a*c)}"
stack = []

for symbol in exp:
    if symbol in '({[':
        stack.append(symbol)
    elif symbol in ')}]':
        if len(stack) == 0:
            print("Not Balanced!")
            break
        elif symbol == ')' and stack[-1] == '(':
            stack.pop()
        elif symbol == '}' and stack[-1] == '{':
            stack.pop()
        elif symbol == ']' and stack[-1] == '[':
            stack.pop()
        else:
            print("Not Balanced!")
            break
else:
    if len(stack) == 0:
        print("Balanced!")
    else:
        print("Not Balanced!")
