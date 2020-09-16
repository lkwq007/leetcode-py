# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         # TLE
#         ret=0
#         nums=list(set(nums))
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 ret=max(ret,nums[i]^nums[j])
#         return ret

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 0<=num<2^31
        template=1<<30
        root=[None,None]
        for item in nums:
            mask=template
            node=root
            while mask>0:
                idx=1 if mask&item else 0
                if node[idx] is None:
                    node[idx]=[None,None]
                node=node[idx]
                mask=mask>>1
        self.ret=0
        node=root
        mask=template
        def test(a,b,mask,acc):
            if a is None or b is None:
                return
            self.ret=max(self.ret,acc)
            flag=True
            if a[0] and b[1]:
                test(a[0],b[1],mask>>1,acc|mask)
                flag=False
            if a[1] and b[0]:
                test(a[1],b[0],mask>>1,acc|mask)
                flag=False
            if flag:
                test(a[0],b[0],mask>>1,acc)
                test(a[1],b[1],mask>>1,acc)
        acc=0
        while node:
            if node[0] and node[1]:
                acc|=mask
                test(node[0],node[1],mask>>1,acc)
                break
            mask=mask>>1
            node=node[0] if node[0] else node[1]
        return max(self.ret,acc)

class Node:
    def __init__(self):
        self.children=[None,None]
        self.endpoint=False

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 0<=num<2^31
        template=1<<30
        root=Node()
        for item in nums:
            mask=template
            node=root
            while mask>0:
                idx=1 if mask&item else 0
                if node.children[idx] is None:
                    node.children[idx]=Node()
                node=node.children[idx]
                mask=mask>>1
            node.endpoint=True
        self.ret=0
        node=root
        mask=template
        def test(a,b,mask,acc):
            if a is None or b is None:
                return
            self.ret=max(self.ret,acc)
            flag=True
            if a.children[0] and b.children[1]:
                test(a.children[0],b.children[1],mask>>1,acc|mask)
                flag=False
            if a.children[1] and b.children[0]:
                test(a.children[1],b.children[0],mask>>1,acc|mask)
                flag=False
            if flag:
                test(a.children[0],b.children[0],mask>>1,acc)
                test(a.children[1],b.children[1],mask>>1,acc)
        acc=0
        while node:
            if node.children[0] and node.children[1]:
                acc|=mask
                test(node.children[0],node.children[1],mask>>1,acc)
                break
            mask=mask>>1
            node=node.children[0] if node.children[0] else node.children[1]
        return max(self.ret,acc)
