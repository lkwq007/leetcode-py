class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(key=lambda x:-x)
        total=len(piles)//3*2
        i=1
        ret=0
        while i<total:
            ret+=piles[i]
            i+=2
        return ret