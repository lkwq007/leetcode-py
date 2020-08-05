class Node:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.left=None
        self.right=None
        self.double=False

class MyCalendarTwo:

    def __init__(self):
        self.root=None

    def search(self,node,start,end,flag):
        if node.start>=end:
            if node.left:
                return self.search(node.left,start,end,flag)
            else:
                if flag:
                    node.left=Node(start,end)
                return True
        elif node.end<=start:
            if node.right:
                return self.search(node.right,start,end,flag)
            else:
                if flag:
                    node.right=Node(start,end)
                return True
        else:
            if node.double:
                return False
            left=True
            right=True
            if start<node.start:
                if node.left:
                    left=self.search(node.left,start,node.start,flag)
                else:
                    left=True
                    if flag:
                        node.left=Node(start,node.start)
                start=node.start
                if not left:
                    return False
            if end>node.end:
                if node.right:
                    right=self.search(node.right,node.end,end,flag)
                else:
                    right=True
                    if flag:
                        node.right=Node(node.end,end)
                end=node.end
                if not right:
                    return False
            if left and right:
                if flag:
                    node.double=True
                    if node.start<start:
                        tmp=Node(node.start,start)
                        tmp.left=node.left
                        node.left=tmp
                        node.start=start
                    if node.end>end:
                        tmp=Node(end,node.end)
                        tmp.right=node.right
                        node.right=tmp
                        node.end=end
                return True
            return False

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root=Node(start,end)
            return True
        if self.search(self.root,start,end,False):
            return self.search(self.root,start,end,True)
        return False

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)