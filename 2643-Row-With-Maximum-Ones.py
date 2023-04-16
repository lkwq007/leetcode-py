class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ret=max([(sum(row),-i) for i,row in enumerate(mat)])
        return -ret[1],ret[0]