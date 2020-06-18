class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k<1:
            return True
        last=-1
        for idx in range(len(nums)):
            if nums[idx]:
                if last!=-1 and idx-last-1<k:
                    return False
                last=idx
        return True

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k<1:
            return True
        cnt=k
        for item in nums:
            if item==0:
                cnt+=1
                continue
            if cnt<k:
                return False
            cnt=0
        return True

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k<1:
            return True
        zeros=k
        last=0
        for item in nums:
            if item==0 and last==1:
                zeros=1
                last=0
            elif item==0:
                zeros+=1
            elif item==1 and last==0:
                if zeros<k:
                    return False
                last=1
            else:
                return False
        return True                