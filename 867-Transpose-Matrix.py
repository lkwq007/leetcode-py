class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # note tha m!=n
        return [[A[y][x] for y in range(len(A))] for x in range(len(A[0]))]