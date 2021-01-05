class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        disjoint=[-1]*len(nums)
        record={}
        for idx in range(len(nums)):
            record[nums[idx]]=idx
        def find(idx):
            tmp=idx
            while disjoint[tmp]>=0:
                tmp=disjoint[tmp]
            ret=tmp
            while disjoint[idx]>=0:
                tmp=disjoint[idx]
                disjoint[idx]=ret
                idx=tmp
            return ret
        def union(a,b):
            a_idx=find(a)
            b_idx=find(b)
            if a_idx!=b_idx:
                if disjoint[a_idx]>disjoint[b_idx]:
                    a_idx,b_idx=b_idx,a_idx
                disjoint[a_idx]+=disjoint[b_idx]
                disjoint[b_idx]=a_idx
        for item in nums:
            idx=record[item]
            if item-1 in record:
                union(record[item-1],idx)
            if item+1 in record:
                union(record[item+1],idx)
        return -min(disjoint)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        record={}
        for item in nums:
            record[item]=1
        def dfs(val):
            if record.get(val,0)!=1:
                return 0
            record[val]=0
            return 1+dfs(val-1)+dfs(val+1)
        ret=0
        for key in record.keys():
            if record[key]==1:
                ret=max(dfs(key),ret)
        return ret