def maxhist(graflist):
    stack = []
    maxsquare = 0
    index = 0

    while(index < len(graflist)):
        if (not stack or (graflist[stack[-1]] <= graflist[index])):
               stack.append(index)
               index += 1
        else:
           top_of_stack = stack.pop()
           square = (graflist[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
           maxsquare = max(maxsquare, square)
    
    while(stack):
      top_of_stack = stack.pop()
      area = (graflist[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
      square = (graflist[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
      maxsquare = max(maxsquare, square)
    
    print(maxsquare)

maxhist([2, 1, 4, 5, 1, 3, 3])
maxhist([3, 3, 3, 3, 3])