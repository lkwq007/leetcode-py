class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if len(arr)<=k:
            return arr
        arr.sort()
        total=len(arr)
        median_idx=(total-1)//2
        median=arr[median_idx]
        ret=[]
        left=0
        right=total-1
        for idx in range(k):
            if arr[right]-median>=median-arr[left]:
                ret.append(arr[right])
                right-=1
            else:
                ret.append(arr[left])
                left+=1
