class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        # sum(nums)=2*sum(arr)
        # N^2?
        # possible k?
        nums.sort()
        n=len(nums)//2
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        for i in range(n):
            k=nums[i+1]-nums[0]
            if k%2 or k==0:
                continue
            cnt=record.copy()
            ret=[]
            for j in range(len(nums)):
                item=nums[j]
                if cnt.get(item,0)>0:
                    cnt[item]-=1
                    if cnt.get(item+k,0)==0:
                        break
                    ret.append(item+k//2)
                    cnt[item+k]-=1
            if len(ret)==n:
                return ret