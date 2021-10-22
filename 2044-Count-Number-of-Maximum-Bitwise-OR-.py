class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        acc=0
        for item in nums:
            acc|=item
        self.ret=0
        def probe(idx,val):
            if idx==len(nums):
                if val==acc:
                    self.ret+=1
                return
            probe(idx+1,nums[idx]|val)
            probe(idx+1,val)
        probe(0,0)
        return self.ret
