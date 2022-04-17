class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # 1 <= nums[i] <= limit <= 10**5
        record={}
        minlst=[0]*(200002)
        maxlst=[0]*(200002)
        for i in range(len(nums)//2):
            val=nums[i]+nums[len(nums)-i-1]
            record[val]=record.get(val,0)+1
            minlst[min(nums[i],nums[len(nums)-i-1])+1]+=1
            maxlst[max(nums[i],nums[len(nums)-i-1])+limit]+=1
        acc=0
        for i in range(len(minlst)):
            acc+=minlst[i]
            minlst[i]=acc
        acc=0
        for i in range(len(maxlst)-1,-1,-1):
            acc+=maxlst[i]
            maxlst[i]=acc
        total=len(nums)//2
        ret=len(nums)
        for i in range(len(maxlst)-1,-1,-1):
            tmp=min(maxlst[i],minlst[i])
            if tmp==total:
                ret=total
                break
        for k,v in record.items():
            cur=total-v
            tmp=min(maxlst[k],minlst[k])
            tmp-=v
            cur=(cur-tmp)*2+tmp
            ret=min(ret,cur)
        return ret