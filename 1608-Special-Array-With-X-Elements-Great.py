class Solution:
    def specialArray(self, nums: List[int]) -> int:
        cnt=[0]*1001
        for item in nums:
            cnt[item]+=1
        acc=0
        for i in range(len(cnt)-1,-1,-1):
            cnt[i]+=acc
            acc=cnt[i]
        for i in range(len(cnt)):
            if cnt[i]==i:
                return i
        return -1