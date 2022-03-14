

def clone_two_dimen_list(l):
    new_list = []

    for row in l:
        new_list += [[number for number in row]]
    
    return new_list


class Stack:

    def __init__(self):
        self.items = []
    def top(self):
        return self.items[-1]
    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items += [item]
    
    def pop(self):
        top = self.top()
        self.items = self.items[ :-1]
        return top
    def length(self):
        return len(self.items)


class Queue:

    def __init__(self):
        self.items = []
        self.length = 0
    def front(self):
        return self.items[0]
    def empty(self):
        return self.length == 0
    
    def push(self, item):
        self.items += [item]
        self.length += 1
    
    def pop(self):
        front = self.front()
        self.items = self.items[1:]
        self.length -= 1
        return front

    def length(self):
        return self.length