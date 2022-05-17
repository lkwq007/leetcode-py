class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 2 pointer also work
        record={0:1}
        cnt=0
        ret=0
        for i in range(len(nums)):
            item=nums[i]
            if item%2:
                cnt+=1
            ret+=record.get(cnt-k,0)
            record[cnt]=record.get(cnt,0)+1
        return ret
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=-1
        right=-1
        ret=0
        cnt=0
        idx=0
        while idx<len(nums):
            if nums[idx]%2:
                cnt+=1
                right=idx
            idx+=1
            if cnt==k:
                break
        if idx==len(nums):
            return 0
        while idx<len(nums):
            if nums[idx]%2:
                lacc=1
                while left+lacc<len(nums) and nums[left+lacc]%2==0:
                    lacc+=1
                ret+=lacc*(idx-right)
                left=left+lacc
                right=idx
            idx+=1
        lacc=1
        while left+lacc<len(nums) and nums[left+lacc]%2==0:
            lacc+=1
        ret+=lacc*(idx-right)
        return ret