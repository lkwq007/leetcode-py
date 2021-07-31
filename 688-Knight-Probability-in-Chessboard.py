class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        # the board is quite small
        queue={(r,c):1.0}
        offset=[]
        for y in [2,-2]:
            for x in [1,-1]:
                offset.append((y,x))
                offset.append((x,y))
        for i in range(K):
            target={}
            for pos,val in queue.items():
                y,x=pos
                nval=val/8
                for yo,xo in offset:
                    yn=y+yo
                    xn=x+xo
                    if 0<=yn<N and 0<=xn<N:
                        target[(yn,xn)]=target.get((yn,xn),0)+nval
            queue=target
        return sum(queue.values())
