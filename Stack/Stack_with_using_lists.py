class Stack():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[len(self.elements) -1]

    def size(self):
        return len(self.elements)

    def reverseStack(self):
        tempStack = Stack()
        while(self.isEmpty() != True):
            tempStack.push(self.pop())
        return tempStack

    def display(self):
        if(self.isEmpty()):
            print("stack is empty")
        else:
            for item in self.elements:
                print(item)



#liste kullanarak stack yazdık.

myStack = Stack()
print(myStack.isEmpty())

myStack.push(16)
myStack.push(35)
myStack.push(6)

print(myStack.peek())

print("myStack : \t ")
myStack.display()

print("reversed myStack : \t")
myStack.reverseStack().display()

