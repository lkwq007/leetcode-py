# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if head is None or head.next is None:
            return len(G)
        G=set(G)
        count=0
        ptr=head
        switch=False
        while ptr:
            if switch and ptr.val not in G:
                switch=False
                count+=1
            elif ptr.val in G:
                switch=True
            ptr=ptr.next
        if switch:
            count+=1
        return count



class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if head is None or head.next is None:
            return len(G)
        mapping=dict()
        for idx,item in enumerate(G,0):
            mapping[item]=idx
        disjoint=[-1]*len(G)
        def find(idx):
            while disjoint[idx]>0:
                idx=disjoint[idx]
            return idx
        def union(v1,v2):
            if v1 in mapping and v2 in mapping:
                idx1=find(mapping[v1])
                idx2=find(mapping[v2])
                if idx1!=idx2:
                    disjoint[idx2]=idx1
        ptr=head
        while ptr:
            if ptr.next:
                union(ptr.val,ptr.next.val)
            ptr=ptr.next
        count=0
        for item in disjoint:
            if item<0:
                count+=1
        return count
