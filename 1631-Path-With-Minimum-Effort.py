class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # can bfs solve this problem?
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        h=len(heights)
        w=len(heights[0])
        queue={(0,0):0}
        record={(0,0):0}
        ret=10**9
        while queue:
            target={}
            for (y0,x0),effort in queue.items():
                if y0==h-1 and x0==w-1:
                    ret=min(ret,effort)
                    continue
                if effort>ret:
                    continue
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    if 0<=y1<h and 0<=x1<w:
                        diff=abs(heights[y1][x1]-heights[y0][x0])
                        tmp=max(effort,diff)
                        if (y1,x1) not in record or record[(y1,x1)]>tmp:
                            target[(y1,x1)]=tmp
                            record[(y1,x1)]=tmp
            queue=target
        return record[(h-1,w-1)]
