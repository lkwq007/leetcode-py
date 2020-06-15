from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy=ListNode(0)
        ptr=dummy
        lists=list(filter(lambda x:x!=None,lists))
        k=len(lists)
        heap=lists
        # build heap
        def parent(i):
            return (i-1)//2
        def left(i):
            return i*2+1
        def right(i):
            return i*2+2
        start=(k//2)-1
        for i in range(start,-1,-1):
            tmp=heap[i]
            while True:
                l=left(i)
                r=right(i)
                smallest=tmp
                if l<k and tmp.val>heap[l].val:
                    smallest=heap[l]
                if r<k and smallest.val>heap[r].val:
                    smallest=heap[r]
                if smallest==tmp:
                    break
                elif smallest==heap[l]:
                    heap[i]=heap[l]
                    i=l
                else:
                    heap[i]=heap[r]
                    i=r
            heap[i]=tmp
        while k>0 and heap[0]:
            ptr.next=heap[0]
            ptr=ptr.next
            heap[0]=heap[0].next
            tmp=heap[0]
            if tmp==None:
                heap[0]=heap[k-1]
                k-=1
                tmp=heap[0]
            i=0
            while left(i)<k:
                if right(i)<k:
                    if tmp.val<heap[left(i)].val and tmp.val<heap[right(i)].val:
                        break
                    else:
                        next=left(i) if heap[left(i)].val<heap[right(i)].val else right(i)
                        heap[i]=heap[next]
                        i=next
                else:
                    if tmp.val<heap[left(i)].val:
                        break
                    else:
                        heap[i]=heap[left(i)]
                        i=left(i)
            heap[i]=tmp
        ptr.next=None
        return dummy.next

def build_list(lst):
    dummy=ListNode(0)
    ptr=dummy
    for item in lst:
        ptr.next=ListNode(item)
        ptr=ptr.next
    return dummy.next

def dump_list(node):
    ptr=node
    while ptr:
        print(ptr.val,end="->")
        ptr=ptr.next

x=Solution()
lst=list(map(build_list,[[2],[1]]))
dump_list(x.mergeKLists(lst))
