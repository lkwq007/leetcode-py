class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low&1==0:
            low+=1
        if high&1==0:
            high-=1
        return (high-low)//2+1