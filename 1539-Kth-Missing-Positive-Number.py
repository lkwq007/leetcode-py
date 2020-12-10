class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # brute force
        num=1
        j=0
        while k>0:
            if j==len(arr) or arr[j]>num:
                k-=1
            else:
                j+=1
            if k==0:
                return num
            num+=1
        return num