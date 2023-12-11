# Abstract Stack Class
class Stack:
    def push(self, element):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

# ListStack Implementation
class ListStack(Stack):
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.elements.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

# LinkedStack Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack(Stack):
    def __init__(self):
        self.top = None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        popped_element = self.top.data
        self.top = self.top.next
        return popped_element

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
list_stack = ListStack()
list_stack.push(1)
list_stack.push(2)
print(list_stack.peek())  
print(list_stack.pop())   
print(list_stack.size())  

linked_stack = LinkedStack()
linked_stack.push('a')
linked_stack.push('b')
print(linked_stack.peek()) 
print(linked_stack.pop())  
print(linked_stack.size())
