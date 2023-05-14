class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        acc=0
        for item in derived:
            acc=acc^item
        return acc==0