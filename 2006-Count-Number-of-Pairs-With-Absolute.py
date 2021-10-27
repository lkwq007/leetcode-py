class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=[0]*201
        ret=0
        for i in range(len(nums)-1,-1,-1):
            item=nums[i]
            ret+=count[item+k]+count[item-k]
            count[item]+=1
        return ret