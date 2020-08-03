class Node:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.left=None # before
        self.right=None # after

class MyCalendar:

    def __init__(self):
        self.root=None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root=Node(start,end)
            return True
        def search(node,start,end):
            if end<=node.start:
                if node.left:
                    return search(node.left,start,end)
                else:
                    node.left=Node(start,end)
                    return True
            elif start>=node.end:
                if node.right:
                    return search(node.right,start,end)
                else:
                    node.right=Node(start,end)
                    return True
            return False
        return search(self.root,start,end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)