class Node:
    def __init__(self):
        self.head=None
        self.times=1
        self.total=0
        self.tail=""
    def __repr__(self):
        return f"[{self.head}],{self.tail},{self.times}"
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        stack=[]
        total=0
        head=Node()
        for item in S:
            if item.isalpha():
                if head.times==1:
                    head.tail+=item
                    head.total+=1
                else:
                    next=Node()
                    next.head=head
                    next.tail+=item
                    next.total=head.total+1
                    head=next
            else:
                times=int(item)
                head.times*=times
                head.total*=times
            if head.total>=K:
                break
        def probe(node,pos):
            # print(node,pos)
            trunk=node.total//node.times
            pos=pos%trunk
            if node.head is None:
                return node.tail[pos]
            else:
                nested_total=node.head.total
                if pos>=nested_total:
                    return node.tail[pos-nested_total]
                else:
                    return probe(node.head,pos)
        return probe(head,K-1)
