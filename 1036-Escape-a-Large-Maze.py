class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # 0 <= blocked.length <= 200, it's impossible to block all paths
        # so we only need to check whethter source and target are surrouned by blocks
        if len(blocked)<2:
            return True
        source=tuple(source)
        target=tuple(target)
        N=1000000
        direction=[(1,0),(0,1),(0,-1),(-1,0)]
        gird={}
        for y,x in blocked:
            gird[(y,x)]=-1
        if source in gird:
            return False
        gird[source]=0
        queue=[source]
        flag=False
        for i in range(len(blocked)):
            target_queue=[]
            for y0,x0 in queue:
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    if (y1,x1)==target:
                        return True
                    if 0<=y1<N and 0<=x1<N and (y1,x1) not in gird:
                        gird[(y1,x1)]=i+1
                        target_queue.append((y1,x1))
            if len(target_queue)==0:
                flag=True
                break
            queue=target_queue
        if flag:
            return False
        gird={}
        for y,x in blocked:
            gird[(y,x)]=-1
        gird[target]=0
        queue=[target]
        flag=False
        for i in range(len(blocked)):
            target_queue=[]
            for y0,x0 in queue:
                for y_offset,x_offset in direction:
                    y1=y0+y_offset
                    x1=x0+x_offset
                    if (y1,x1)==source:
                        return True
                    if 0<=y1<N and 0<=x1<N and (y1,x1) not in gird:
                        gird[(y1,x1)]=i+1
                        target_queue.append((y1,x1))
            if len(target_queue)==0:
                flag=True
                break
            queue=target_queue
        if flag:
            return False
        return True