class Node:
    def __init__(self,parent):
        self.val=0
        self.next=None
        self.prev=None
        self.parent=parent

class ListNode:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
        self.head=Node(self)
        self.tail=Node(self)
        self.head.next=self.tail
        self.tail.prev=self.head

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.mapping={}
        self.chain=ListNode(0)
        tail=ListNode(-1)
        self.chain.next=tail
        tail.prev=self.chain
    
    def inc(self,node:Node):
        parent=node.parent
        parent.head.val-=1
        node.prev.next=node.next
        node.next.prev=node.prev
        if parent.next.val!=parent.val+1:
            inc=ListNode(parent.val+1)
            inc.next=parent.next
            inc.prev=parent
            parent.next=inc
            inc.next.prev=inc
        else:
            inc=parent.next
        inc.head.val+=1
        node.next=inc.head.next
        node.prev=inc.head
        inc.head.next=node
        node.next.prev=node
        node.parent=inc
        if parent.head.val==0 and parent.val>0:
            parent.next.prev=parent.prev
            parent.prev.next=parent.next
            del parent

    def get(self, key: int) -> int:
        if key in self.mapping:
            node,val=self.mapping[key]
            self.inc(node)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node,val=self.mapping[key]
        else:
            if self.capacity==0:
                least_freq=self.chain.next
                if least_freq.val>0:
                    least_recent=least_freq.tail.prev
                    least_recent.next.prev=least_recent.prev
                    least_recent.prev.next=least_recent.next
                    least_freq.head.val-=1
                    del self.mapping[least_recent.val]
                    if least_freq.head.val==0 and least_freq.val>0:
                        least_freq.next.prev=least_freq.prev
                        least_freq.prev.next=least_freq.next
                else:
                    return
            else:
                self.capacity-=1
            node=Node(self.chain)
            node.next=self.chain.head.next
            node.prev=self.chain.head
            node.next.prev=node
            node.prev.next=node
        self.inc(node)
        self.mapping[key]=(node,value)
        node.val=key

            

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)