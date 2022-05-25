class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr)<2:
            return 0
        left=len(arr)
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                left=i
                break
        if left==len(arr):
            return 0
        right=-1
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>arr[i+1]:
                right=i
                break
        ret=min(len(arr)-left,right+1)
        idx=right+1
        for i in range(left):
            cur=arr[i]
            while idx<len(arr) and arr[idx]<cur:
                idx+=1
            ret=min(ret,idx-i-1)
        idx=left-1
        for i in range(len(arr)-1,right,-1):
            cur=arr[i]
            while idx>=0 and arr[idx]>cur:
                idx-=1
            ret=min(ret,i-idx-1)
        return ret
