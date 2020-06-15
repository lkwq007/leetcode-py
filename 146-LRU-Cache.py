class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.total=capacity
        self.cnt=0
        self.mapping={}
        self.dummy=ListNode(None,None)
        self.dummy.next=self.dummy
        self.dummy.prev=self.dummy
    
    def move(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        node.next=self.dummy
        node.prev=self.dummy.prev
        node.prev.next=node
        self.dummy.prev=node

    def get(self, key: int) -> int:
        if key in self.mapping:
            node=self.mapping[key]
            self.move(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.total<1:
            return
        if key in self.mapping:
            node=self.mapping[key]
            self.move(node)
            node.val=value
        elif self.cnt<self.total:
            self.cnt+=1
            node=ListNode(key,value)
            self.mapping[key]=node
            node.next=self.dummy
            node.prev=self.dummy.prev
            node.prev.next=node
            node.next.prev=node
        else:
            removed=self.dummy.next
            del self.mapping[removed.key]
            self.mapping[key]=removed
            removed.key=key
            removed.val=value
            self.move(removed)





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)