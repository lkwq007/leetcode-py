class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ret={}
        def probe(i,lst):
            if i==len(nums):
                if len(lst)>1:
                    self.ret[tuple(lst)]=1
                return
            if len(lst)<1 or nums[i]>=lst[-1]:
                lst.append(nums[i])
                probe(i+1,lst)
                lst.pop()
            probe(i+1,lst)
        probe(0,[])
        return list(self.ret.keys())