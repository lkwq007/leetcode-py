class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr)-1:
            return max(arr)
        cnt=0
        cur=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>cur:
                cnt=1
                cur=arr[i]
            else:
                cnt+=1
            if cnt==k:
                return cur
        return cur