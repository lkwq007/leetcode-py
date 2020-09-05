class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices%2==1 or tomatoSlices<2*cheeseSlices:
            return []
        jumbo=(tomatoSlices-2*cheeseSlices)//2
        small=cheeseSlices-jumbo
        if jumbo>=0 and small>=0:
            return [jumbo,small]
        return []