class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums.sort()
        def probe(i):
            if i==len(nums)-1:
                return {nums[i]:1,-nums[i]:1} if nums[i]!=0 else {nums[i]:2}
            record={}
            lst=probe(i+1)
            for cur in (nums[i],-nums[i]):
                for k,v in lst.items():
                    record[cur+k]=record.get(cur+k,0)+v
            return record
        lst=probe(0)
        return lst.get(S,0)