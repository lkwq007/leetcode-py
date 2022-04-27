class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        record=[0]*1001
        for lst in nums:
            for item in lst:
                record[item]+=1
        ret=[]
        for i in range(1001):
            if record[i]==len(nums):
                ret.append(i)
        return ret