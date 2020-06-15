class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-n+1,n,2))