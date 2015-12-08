'''
Write a program to sort a stack such that the smallest items are on the top.
You may use at most one additional stack to hold items,
but you may not copy the elements into any other data structure(such as an array).
The stack supports the following operations: push, pop, peek, and isEmpty.
'''

def sort_stack(primary_stack):
    secondary_stack = []
    while primary_stack:
        temp = primary_stack.pop()
        while secondary_stack and secondary_stack[-1] > temp:
            primary_stack.append(secondary_stack.pop())

        secondary_stack.append(temp)

    return secondary_stack


primary_stack = [7, 10, 12, 8, 1, 3]
print sort_stack(primary_stack)
