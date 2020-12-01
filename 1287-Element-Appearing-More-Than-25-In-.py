class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        total=len(arr)
        target=total//4
        cnt=0
        cur=arr[0]-1
        for i in range(total):
            if arr[i]==cur:
                cnt+=1
            else:
                cur=arr[i]
                cnt=1
            if cnt>target:
                return arr[i]