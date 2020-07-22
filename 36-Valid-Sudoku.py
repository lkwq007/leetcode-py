class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        base=ord("0")
        get=[lambda i,j: board[i][j],lambda i,j: board[j][i],lambda i,j: board[i//3*3+j//3][(i%3)*3+j%3]]            
        def validate(i,direction,cnt):
            for j in range(9):
                item=get[direction](i,j)
                if item!=".":
                    item=ord(item)-base
                    cnt[item]+=1
                    if cnt[item]>1:
                        return False
            return True
        count=[0]*10
        # 9x9
        for i in range(9):
            for direction in range(3):
                if not validate(i,direction,count[:]):
                    return False
        return True