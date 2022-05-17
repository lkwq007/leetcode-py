class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ret=max(top-special[-1],special[0]-bottom)
        for i in range(1,len(special)):
            ret=max(ret,special[i]-special[i-1]-1)
        return ret


