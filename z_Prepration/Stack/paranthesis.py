def ValidParanthesis(s):
    stack = []
    
    for ch in s:

        if ch in ["(", "{", "["]:
            stack.append(ch)
        

        elif ch in [")", "}", "]"]:
            

            if len(stack) == 0:
                return False
            
            top = stack[-1]

            if (ch == ")" and top == "(") or \
               (ch == "}" and top == "{") or \
               (ch == "]" and top == "["):
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(ValidParanthesis("()[]{}"))  
print(ValidParanthesis("()[]}"))   
