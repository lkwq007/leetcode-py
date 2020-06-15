# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cnt=0
        ptr=root
        while ptr:
            cnt+=1
            ptr=ptr.next
        ret=[]
        lens=cnt//k
        remain=cnt%k
        ret_cnt=[lens]*k
        for i in range(0,remain):
            ret_cnt[i]+=1
        ptr=root
        for i in range(0,k):
            if ret_cnt[i]>0:
                ret.append(ptr)
                for i in range(0,ret_cnt[i]-1):
                    ptr=ptr.next
                tmp=ptr
                ptr=ptr.next
                tmp.next=None       
            else:
                ret.append(None)
        return ret
        