LIST_1 = input()
stack = []
for each_bracket in LIST_1:
    if(each_bracket == '[' or each_bracket == '{' or each_bracket == '(' ):
        stack.append(each_bracket)
    else:
        top = stack[-1]
        if(top == '(' and each_bracket ==')'):
            stack.pop()
        elif(top == '[' and each_bracket ==']'):
            stack.pop()
        elif(top == '{' and each_bracket == '}'):
            stack.pop()
        else:
            stack.append(each_bracket)
if(len(stack) == 0):
    print("Brackets are Satisfied")
else:
    print("Brackets are not Satisfied")            
