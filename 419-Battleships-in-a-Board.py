class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # only valid board
        cnt=0
        h,w=len(board),len(board[0])
        for y in range(h):
            for x in range(w):
                left="." if x==0 else board[y][x-1]
                top="." if y==0 else board[y-1][x]
                if left=="." and top=="." and board[y][x]=="X":
                    cnt+=1
        return cnt