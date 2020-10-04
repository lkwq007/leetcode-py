class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 2x3
        initial=tuple((board[i//3][i%3] for i in range(6)))
        final=(1,2,3,4,5,0)
        if initial==final:
            return 0
        queue=[initial]
        step=0
        visited={}
        visited[initial]=1
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            target=[]
            step+=1
            for state in queue:
                template=list(state)
                for i in range(6):
                    if template[i]==0:
                        break
                y=i//3
                x=i%3
                for offset in (-1,1):
                    if 0<=x+offset<3:
                        template[i],template[i+offset]=template[i+offset],template[i]
                        next=tuple(template)
                        if next==final:
                            return step
                        template[i],template[i+offset]=template[i+offset],template[i]
                        if next not in visited:
                            visited[next]=1
                            target.append(next)
                idx=(1-y)*3+x
                template[idx],template[i]=template[i],template[idx]
                next=tuple(template)
                if next==final:
                    return step
                if next not in visited:
                    visited[next]=1
                    target.append(next)
            queue=target
        return -1
                
