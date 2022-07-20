class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # using data range
        cur=1001
        ret=0
        for i in range(len(nums)):
            if nums[i]<1001:
                idx=i
                sign=1 if nums[i]>0 else 0
                while True:
                    next=(idx+nums[idx]+len(nums))%len(nums)
                    nums[idx]=cur
                    next_sign=1 if nums[next]>0 else 0
                    if nums[next]==cur and next!=idx:
                        ret+=1
                        break
                    elif sign!=next_sign or nums[next]>1000:
                        break
                    idx=next
                cur+=1
        return ret
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # two pointer
        total=len(nums)
        def iter(idx,sign):
            idx=(idx+nums[idx]+total)%total
            return idx, sign!=int(nums[idx]>0) or nums[idx]==0 or nums[idx]%total==0
        ret=0
        for i in range(len(nums)):
            if nums[i]%total==0:
                continue
            fast=i
            slow=i
            sign=int(nums[i]>0)
            flag=True
            while True:
                slow, status=iter(slow,sign)
                if status:
                    flag=False
                    break
                fast, status=iter(fast,sign)
                if status:
                    flag=False
                    break
                fast, status=iter(fast,sign)
                if status:
                    flag=False
                    break
                if fast==slow:
                    break
            if flag:
                ret+=1
            slow=i
            while True:
                nums[slow]=0
                slow, status=iter(slow,sign)
                if status:
                    nums[slow]=0
                    break
        return ret
