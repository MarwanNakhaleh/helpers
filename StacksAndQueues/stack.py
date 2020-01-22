class StackOnList:
    def __init__(self):
        self.stack = []

    def push(self, data=None):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("cannot pop an empty stack")
            return None
        to_return = self.stack[-1]
        self.stack = self.stack[:-1] # removes last element from stack
        return to_return

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
if __name__ == "__main__":
    stacc = StackOnList()
    stacc.push(8008)
    print(stacc.stack)
    stacc.push(69)
    print(stacc.stack)
    stacc.push(420)
    print(stacc.stack)
    print(stacc.pop())
    print(stacc.stack)