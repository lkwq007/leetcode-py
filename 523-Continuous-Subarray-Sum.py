class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if (k==1 or k==-1) and len(nums)>1:
            return True
        record={0:-1}
        acc=0
        for idx in range(len(nums)):
            item=nums[idx]
            acc+=item
            tmp=acc%k if k else acc
            if tmp in record:
                if idx-record[tmp]>1:
                    return True
            else:
                record[tmp]=idx
        return False