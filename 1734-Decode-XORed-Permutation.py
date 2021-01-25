class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        acc=len(encoded)+1
        for i,item in enumerate(encoded,1):
            acc^=i^item
        