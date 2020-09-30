class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees=[]
        h=len(forest)
        w=len(forest[0])
        for y in range(h):
            for x in range(w):
                if forest[y][x]>1:
                    trees.append(forest[y][x])
        tempalte=[0]*w
        visited=[tempalte[:] for _ in range(h)]
        queue=[(0,0)]
        visited[0][0]=1
        trees.sort()
        total=len(trees)
        idx=0 if forest[0][0]!=trees[0] else 1
        if idx==total:
            return 0
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        step=0
        bound=0
        while queue:
            target=[]
            step+=1
            flag=False
            for y0,x0 in queue:
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    if 0<=y1<h and 0<=x1<w:
                        if forest[y1][x1]==trees[idx]:
                            visited[y1][x1]=step
                            bound=step
                            target=[(y1,x1)]
                            idx+=1
                            flag=True
                            break
                        elif forest[y1][x1]!=0 and visited[y1][x1]<=bound:
                            visited[y1][x1]=step
                            target.append((y1,x1))
                if flag:
                    break
            if idx==total:
                return step
            queue=target
        return -1