class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ret=set([])
        def probe(idx,lst):
            if idx==len(nums):
                self.ret.add(tuple(lst))
                return
            probe(idx+1,lst)
            lst.append(nums[idx])
            probe(idx+1,lst)
            lst.pop()
        probe(0,[])
        return list(self.ret)