class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ret=[0]*len(spells)
        for i in range(len(spells)):
            spell=spells[i]
            need=(success+spell-1)//spell
            left=0
            right=len(potions)
            while left<right:
                middle=left+(right-left)//2
                if potions[middle]<need:
                    left=middle+1
                else:
                    right=middle
            ret[i]=len(potions)-left
        return ret