class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.total=k
        self.cnt=0
        self.buffer=[0]*k
        self.front=0
        self.rear=-1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.cnt==self.total:
            return False
        self.cnt+=1
        self.front-=1
        self.buffer[self.front]=value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.cnt==self.total:
            return False
        self.cnt+=1
        self.rear+=1
        self.buffer[self.rear]=value
        return True        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.cnt==0:
            return False
        self.cnt-=1
        self.front+=1
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.cnt==0:
            return False
        self.cnt-=1
        self.rear-=1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.cnt==0:
            return -1
        return self.buffer[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.cnt==0:
            return -1
        return self.buffer[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cnt==0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cnt==self.total


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()