# STACKS

# Peek : get item on top of stack, without removing it.
#Clear : all items from stack


#STACKS < QUEUES & HEAPS

'''
Stack using Python List
Stack is a LIFO data structure : last in , first out 
Use append() to push an item onto the stack.
Use pop() to remove an item 
'''

my_stack = list()
my_stack.append(4)
my_stack.append(14)
my_stack.append(45)
my_stack.append(84)
my_stack.append(49)
print(my_stack)

# append() function push item in the stack 

print(my_stack.pop()) # push last item out of the stack

# Stack using List with a wrapper class
'''
we create a stack class and a full set of Stack methods.
But the underlying data structure is really a python List.
For pop and peek methods we first check whether the stack is empty, to avoid exceptio s

'''

class Stack:
    def __init__(self):
        self.stack = list()
    
    def push (self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek (self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) -1]
        else:
            return None
    
    def __str__(self):
        return str(self.stack)
    
my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())