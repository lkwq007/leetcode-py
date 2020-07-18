class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        term=10**9+7
        masks=[0]*41
        mask=1
        for i in range(40):
            masks[i+1]=mask
            mask=mask<<1
        