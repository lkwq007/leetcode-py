class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        total=len(target)
        # brute force
        ret=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and len(nums[i])+len(nums[j])==total and nums[i]+nums[j]==target:
                    ret+=1
        return ret

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        record={}
        for item in nums:
            if item not in record:
                record[item]=0
            record[item]+=1
        ret=0
        for i in range(1,len(target)):
            left=target[:i]
            right=target[i:]
            if left in record and right in record:
                if left==right:
                    ret+=record[left]*(record[left]-1)
                else:
                    ret+=record[left]*record[right]
        return ret