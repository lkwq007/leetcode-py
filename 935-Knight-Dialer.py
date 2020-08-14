class Solution:
    def knightDialer(self, N: int) -> int:
        if N<2:
            return 10
        mapping=[[4,6],[6,8],[7,9],[4,8],[3,9],[],[1,7],[2,6],[1,3],[2,4]]
        cnt=[]