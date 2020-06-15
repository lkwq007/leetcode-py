class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret=[False]*len(candies)
        max_val=max(candies)
        for idx in range(0,len(candies)):
            if candies[idx]+extraCandies>=max_val:
                ret[idx]=True
        return ret