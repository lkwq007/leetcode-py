class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret=set([])
        def probe(i,lst):
            if i==len(nums):
                ret.add(tuple([nums[item] for item in lst]))
                return
            for idx in range(len(nums)):
                if idx not in lst:
                    lst.append(idx)
                    probe(i+1,lst)
                    lst.pop()
        probe(0,[])
        return [list(item) for item in ret]