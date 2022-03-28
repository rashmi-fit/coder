# Stack class, init is the constructor here, option+shift+F to reformat the code which will remove extra space in VS

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
        # retuen not self.items

    def push(self, items):
        self.items.append(items)

    def pop(self, items):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.size())

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop(5))
    print(s)
    print(s.peek())
    print(s.size())
