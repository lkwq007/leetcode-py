class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ret=0
        for item in costs:
            if item<=coins:
                ret+=1
                coins-=item
            if coins<item:
                break
        return ret