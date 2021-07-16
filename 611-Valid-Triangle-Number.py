class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 0 <= nums[i] <= 1000
        cnt=[0]*1001
        for item in nums:
            cnt[item]+=1
        prefix=[0]*2002
        acc=0
        for i in range(len(cnt)):
            acc+=cnt[i]
            prefix[i]=acc
        for i in range(len(cnt),len(prefix)-1):
            prefix[i]=acc
        lst=[i for i in range(1,1001) if cnt[i]>0]
        ret=0
        for i in range(len(lst)):
            vi=lst[i]
            if cnt[vi]>2:
                ret+=cnt[vi]*(cnt[vi]-1)*(cnt[vi]-2)//2//3
            for j in range(i+1,len(lst)):
                vj=lst[j]
                if cnt[vj]>1:
                    ret+=cnt[vi]*cnt[vj]*(cnt[vj]-1)//2
                if cnt[vi]>1 and vi*2>vj:
                    ret+=cnt[vi]*(cnt[vi]-1)*cnt[vj]//2
                ret+=cnt[vi]*cnt[vj]*(prefix[vi+vj-1]-prefix[vj])
        return ret

