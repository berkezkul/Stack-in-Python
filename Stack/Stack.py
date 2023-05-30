class Stack:
    def __init__(self, size):
        self.top = -1
        self.items = [None] * size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.items) - 1

    def count(self):                               #number of elements of the stack
        return self.top + 1

    def size(self):                                #stack's capacity
        return len(self.items)

    def peek(self):
        if (self.is_empty() == False):
            return self.items[self.top]
        else:
            print("Stack is empty")
            return None

    def push(self, val):
        if self.is_full():
            print("Stack is full")
        else:
            self.top += 1
            self.items[self.top] = val

    def pop(self):
        if (self.is_empty()):
            print("Stack is empty")
            return -1
        else:
            self.top -= 1
            return self.items[self.top + 1]

    def display(self):
        if (self.is_empty()):
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):         #decreases by 1 towards the -1. index.
                print(self.items[i])


myStack = Stack(6)
myStack.push(5)
myStack.push(12)
myStack.push(13)
print("myStack count:", myStack.count())
print("myStack size:", myStack.size())
myStack.display()


#first in last out-> Stack
#first in first out-> Queue