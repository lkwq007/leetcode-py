class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        template=[0]*8
        board=[template[:] for _ in range(8)]
        for y,x in queens:
            board[y][x]=1
        direction=[-1,0,1]
        ret=[]
        for y_offset in direction:
            for x_offset in direction:
                if y_offset==0 and x_offset==0:
                    continue
                y,x=king
                while 0<=y<8 and 0<=x<8:
                    if board[y][x]==1:
                        ret.append([y,x])
                        break
                    y+=y_offset
                    x+=x_offset
        return ret
