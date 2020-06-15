# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ptr=head
        buffer=[]
        while ptr:
            buffer.append(ptr.val)
            ptr=ptr.next
        total=len(buffer)
        ret=[0]*total
        idx=2
        while idx<=total:
            if buffer[-idx]<buffer[-idx+1]:
                ret[-idx]=-idx+1
            elif buffer[-idx]>buffer[-idx+1]:
                tmp=ret[-idx+1]
                while tmp!=0:
                    if buffer[-idx]<buffer[tmp]:
                        ret[-idx]=tmp
                        break
                    else:
                        tmp=ret[tmp]
                if tmp==0:
                    ret[-idx]=0
            else:
                ret[-idx]=ret[-idx+1]
            idx+=1
        for idx in range(0,total):
            if ret[idx]:
                tmp=ret[idx]
                ret[idx]=buffer[tmp]
        return ret