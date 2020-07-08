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
