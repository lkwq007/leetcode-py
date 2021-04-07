class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        record={}
        acc=0
        ret=len(nums)
        total=sum(nums)
        rest=total%p
        if rest==0:
            return 0
        if total<p:
            return -1
        record[0]=-1
        for i in range(len(nums)):
            acc+=nums[i]
            nums[i]=acc
            cur=acc%p
            tmp=(cur-rest+p)%p
            record[cur]=i
            if tmp in record:
                ret=min(ret,i-record[tmp])
        return -1 if ret==len(nums) else ret