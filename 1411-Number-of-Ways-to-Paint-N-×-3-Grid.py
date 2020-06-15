class Solution:
    def numOfWays(self, n: int) -> int:
        unique=6
        same=6
        term=10**9+7
        for idx in range(1,n):
            unique,same=(unique*2+same*2)%term,(unique*2+same*3)%term
        return (unique+same)%term
        