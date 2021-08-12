class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total%k!=0:
            return False
        part=total//k
        nums.sort()
        import functools
        target=(part,)*(k-1)
        @functools.lru_cache(maxsize=None)
        def probe(lst,acc):
            if lst==target:
                return True
            mask=1
            flag=False
            for i in range(len(nums)):
                if mask&acc:
                    continue
                tmp=list(lst)
                for j in range(len(tmp)):
                    tmp[j]+=nums[i]
                    if tmp[j]<=part:
                        flag=flag or probe(tuple(sorted(tmp)),acc|mask)
                    tmp[j]-=nums[i]
                    if flag:
                        return True
                mask=mask<<1
            return flag
        return probe((0,)*(k-1),0)