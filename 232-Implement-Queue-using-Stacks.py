class Stack:
    def __init__(self):
        self.stack=[]
    def size(self):
        return len(self.stack)
    def push(self,x):
        self.stack.append(x)
    def peek(self):
        return self.stack[-1]
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack)==0

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=Stack()
        self.bak=Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while not self.stack.is_empty():
            tmp=self.stack.pop()
            self.bak.push(tmp)
        self.stack.push(x)
        while not self.bak.is_empty():
            tmp=self.bak.pop()
            self.stack.push(tmp)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack.peek()
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()