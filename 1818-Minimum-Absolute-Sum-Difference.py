class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        total=sum([abs(a-b) for a,b in zip(nums1,nums2)])
        lst=nums1[:]
        lst.sort()
        acc=0
        for i in range(len(nums1)):
            val1=nums1[i]
            val2=nums2[i]
            if val1==val2:
                continue
            left=0
            right=len(lst)
            while left<right:
                middle=left+(right-left)//2
                if lst[middle]==val2:
                    break
                elif lst[middle]<val2:
                    left=middle+1
                else:
                    right=middle
            target=abs(val1-val2)
            for idx in range(middle-1,middle+2):
                if 0<=idx<len(lst):
                    target=min(target,abs(lst[idx]-val2))
            acc=max(abs(val1-val2)-target,acc)
        return (total-acc)%(10**9+7)