class Queue:
    def __init__(self):
        self.idx=0
        self.len=0
        self.queue=[]
    def size(self):
        return self.len
    def is_empty(self):
        return self.len==0
    def push(self,val):
        self.queue.append(val)
        self.len+=1
    def peek(self):
        return self.queue[self.idx]
    def pop(self):
        self.idx+=1
        self.len-=1
        return self.queue[self.idx-1]

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        size=self.queue.size()
        self.queue.push(x)
        idx=0
        while idx<size:
            tmp=self.queue.pop()
            self.queue.push(tmp)
            idx+=1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue.peek()
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()