class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt=[0]*101
        for item in nums:
            cnt[item]+=1
        acc=0
        for idx in range(len(cnt)):
            acc,cnt[idx]=acc+cnt[idx],acc
        return [cnt[item] for item in nums]
        
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        record={}
        for item in nums:
            if item in record:
                record[item]+=1
            else:
                record[item]=1
        acc=0
        for key,cnt in sorted(record.items()):
            tmp=acc+cnt
            record[key]=acc
            acc=tmp
        ret=[0]*len(nums)
        for idx in range(len(nums)):
            ret[idx]=record[nums[idx]]
        return ret