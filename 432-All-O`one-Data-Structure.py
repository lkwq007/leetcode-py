class ListNode:
    def __init__(self) -> None:
        self.next=None
        self.prev=None
        self.val=0
        self.lst={}
    
    def __repr__(self) -> str:
        return str(self.val)+":"+str(self.lst)+">"

class AllOne:

    def __init__(self):
        self.record={}
        self.node_record={}
        self.head=ListNode()
        self.head.val=0
        self.tail=ListNode()
        self.tail.val=-1
        self.head.next=self.tail
        self.tail.prev=self.head
        self.node_record[0]=self.head
    
    def print(self):
        print("===")
        print(self.node_record)
        ptr=self.head
        while ptr:
            print(ptr)
            ptr=ptr.next
    
    def clean(self,node):
        if len(node.lst)==0 and node.val!=0 and node.val!=-1:
            node.prev.next=node.next
            node.next.prev=node.prev
            del self.node_record[node.val]

    def inc(self, key: str) -> None:
        # update record
        if key not in self.record:
            self.record[key]=0
        self.record[key]+=1
        cur=self.record[key]
        # update lst
        last=self.node_record[cur-1]
        if cur!=1:
            del last.lst[key]
        if cur not in self.node_record:
            node=ListNode()
            self.node_record[cur]=node
            node.val=cur
            node.next=last.next
            node.prev=last
            node.next.prev=node
            last.next=node
        self.node_record[cur].lst[key]=1
        self.clean(last)

    def dec(self, key: str) -> None:
        # update record
        self.record[key]-=1
        cur=self.record[key]
        if cur==0:
            del self.record[key]
        # update lst
        last=self.node_record[cur+1]
        del last.lst[key]
        if cur!=0:
            if cur not in self.node_record:
                node=ListNode()
                self.node_record[cur]=node
                node.val=cur
                node.next=last
                node.prev=last.prev
                node.next.prev=node
                node.prev.next=node
            self.node_record[cur].lst[key]=1
        self.clean(last)
        

    def getMaxKey(self) -> str:
        for k in self.tail.prev.lst.keys():
            return k
        return ""

    def getMinKey(self) -> str:
        for k in self.head.next.lst.keys():
            return k
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()