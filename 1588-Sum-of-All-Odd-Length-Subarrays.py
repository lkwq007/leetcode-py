class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=len(arr)
        ret=0
        for i in range(total):
            if i==0 or i==total-1:
                ret+=(total+1)//2*arr[i]
            else:
                cnt=((i+2)//2)*((total-i+1)//2)+((i+1)//2)*((total-i)//2)
                ret+=cnt*arr[i]
        return ret