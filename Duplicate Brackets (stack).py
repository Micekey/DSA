#This program verfies if the expression has duplicate brackets or not.
exp = "(a+b)+(c+d)"
stack = []

for symbol in exp:
    if symbol == ")":
        if stack[-1] == "(":
            print("true")
            break
        else:
            while stack[-1] != "(":
                stack.pop()
            stack.pop()
    else:
        stack.append(symbol)
else:
    print("false")
