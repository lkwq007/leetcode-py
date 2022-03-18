class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # simple one pass
        ret=target[0]
        for i in range(1,len(target)):
            ret+=max(0,target[i]-target[i-1])
        return ret

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # mono stack
        stack=[]
        ret=0
        for i in range(len(target)):
            item=target[i]
            top=stack[-1] if stack else item
            while stack and stack[-1]>=item:
                stack.pop()
            ret+=max(top-item,0)
            stack.append(item)
            # print(stack,ret)
        return ret+max(stack)

class ListNode:
    def __init__(self,val=0) -> None:
        self.next=None
        self.prev=None
        self.val=val    
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # 1 <= target.length <= 10^5
        # brute force
        record={}
        head=ListNode()
        tail=ListNode()
        head.next=tail
        tail.prev=head
        for i in range(len(target)):
            if i>0 and target[i]==target[i-1]:
                pass
            else:
                if target[i] not in record:
                    record[target[i]]=[]
                node=ListNode(target[i])
                node.next=tail
                node.prev=tail.prev
                node.prev.next=node
                tail.prev=node
                record[target[i]].append(node)
        keys=list(record.keys())
        keys.sort(key=lambda x:-x)
        ret=0
        for i in range(len(keys)-1):
            key=keys[i]
            for node in record[key]:
                ret+=key-max(node.next.val,node.prev.val)
                node.prev.next=node.next
                node.next.prev=node.prev
        ret+=keys[-1]
        return ret