def valid(str):

    stack = []

    close = { ')' : '(', ']' : '[', '}' :  '{'}

    for c in str:

        if c in close:

            if stack and stack[-1] == close[c]:

                stack.pop()
            
            else:

                return False
        
        else:

            stack.append(c)

    return  True if not stack else False







