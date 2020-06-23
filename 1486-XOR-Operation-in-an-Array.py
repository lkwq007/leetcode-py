class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        end=start+2*n
        acc=0
        for item in range(start,end,2):
            acc^=item
        return acc