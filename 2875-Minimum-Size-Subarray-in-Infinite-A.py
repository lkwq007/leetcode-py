class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        # 1 <= nums[i] <= 10^5
        total=sum(nums)
        right=[0]*(len(nums)+1)
        left=[0]*(len(nums)+1)
        record={}
        record[0]=0
        for i in range(len(nums)):
            left[i+1]=left[i]+nums[i]
            right[i+1]=right[i]+nums[len(nums)-i-1]
            cur=right[i+1]
            record[cur]=i+1
        ret=-1
        if target==total:
            return len(nums)
        div=target//total*len(nums)
        target%=total
        for i in range(len(left)):
            cur=left[i]
            rest=target-cur
            if rest in record:
                val=div+i+record[rest]
                if ret==-1 or val<ret:
                    ret=val
            rest=total-target-cur
            if rest in record:
                val=div+len(nums)-i-record[rest]
                if ret==-1 or val<ret:
                    ret=val
        return ret
