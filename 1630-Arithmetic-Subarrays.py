class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # brute force
        ret=[False]*len(l)
        idx=0
        for left,right in zip(l,r):
            acc=0
            total=right-left+1
            min_val=nums[left]
            max_val=nums[right]
            record={}
            for i in range(left,right+1):
                record[nums[i]]=record.get(nums[i],0)+1
                min_val=min(min_val,nums[i])
                max_val=max(max_val,nums[i])
            diff=max_val-min_val
            if diff==0:
                ret[idx]=True
            elif diff%(total-1)==0:
                flag=True
                diff=diff//(total-1)
                for i in range(min_val,max_val+1,diff):
                    if record.get(i,0)!=1:
                        flag=False
                ret[idx]=flag
            idx+=1
        return ret