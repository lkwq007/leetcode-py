class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        lst=str(num)
        ret=0
        for i in range(len(lst)-k+1):
            cur=int(lst[i:i+k])
            if cur!=0 and num%cur==0:
                ret+=1
        return ret