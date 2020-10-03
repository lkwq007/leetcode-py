class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        h=len(grid)
        w=len(grid[0])
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        self.queue=[]
        self.counter=[]
        self.target=[]
        self.cnt=0
        size=h*w
        self.mark=2
        def dfs(y0,x0):
            self.cnt+=1
            walls=0
            grid[y0][x0]=2
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=x1<w and 0<=y1<h:
                    if grid[y1][x1]==0:
                        self.queue[-1][(y1,x1)]=1
                        walls+=1
                    elif grid[y1][x1]==1:
                        walls+=dfs(y1,x1)
            return walls
        for y in range(h):
            for x in range(w):
                if grid[y][x]==1:
                    self.queue.append({})
                    walls=dfs(y,x)
                    self.counter.append(walls)
        self.total=len(self.queue)
        self.walls=0
        def build():
            max_idx=0
            for i in range(self.total):
                if len(self.queue[max_idx])<len(self.queue[i]):
                    max_idx=i
            self.walls+=self.counter[max_idx]
            if max_idx!=self.total-1:
                self.queue[max_idx]=self.queue[-1]
                self.counter[max_idx]=self.counter[-1]
            self.queue.pop()
            self.counter.pop()
            self.total-=1
        def find(lst,x):
            if lst[x]==x:
                return x
            lst[x]=find(lst,lst[x])
            return lst[x]
        def dfs2(y0,x0,idx,mapping):
            tmp=grid[y0][x0]
            grid[y0][x0]=self.mark
            walls=0
            self.cnt+=1
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w:
                    if grid[y1][x1]<0:
                        if grid[y1][x1]!=tmp:
                            idx2=find(mapping,-grid[y1][x1]-1)
                            mapping[idx2]=idx
                        walls+=dfs2(y1,x1,idx,mapping)
                    elif grid[y1][x1]==0:
                        self.target[idx][(y1,x1)]=1
                        walls+=1
            return walls
        def contaminate():
            mapping=[i for i in range(self.total)]
            # update the whole grid
            for i in range(self.total):
                keys=self.queue[i].keys()
                for y0,x0 in keys:
                    if grid[y0][x0]==0:
                        grid[y0][x0]=-i-1
                    else:
                        idx1=find(mapping,i)
                        idx2=find(mapping,-grid[y0][x0]-1)
                        mapping[idx1]=idx2
            # do dfs
            self.counter=[0]*self.total
            self.target=[{} for _ in range(self.total)]
            for i in range(self.total):
                keys=self.queue[i].keys()
                for y0,x0 in keys:
                    if grid[y0][x0]<0:
                        idx=find(mapping,i)
                        tmp=dfs2(y0,x0,idx,mapping)
                        self.counter[idx]+=tmp
            oldcounter=self.counter
            for i in range(self.total):
                if mapping[i]!=i:
                    idx=find(mapping,i)
                    self.counter[idx]+=self.counter[i]
                    for key in self.target[i].keys():
                        self.target[idx][key]=1
            idxs=set([find(mapping,i) for i in range(self.total)])
            self.queue=[self.target[i] for i in idxs]
            self.counter=[self.counter[i] for i in idxs]
            self.total=len(self.queue)
        while self.cnt<size and self.total>0:
            build()
            self.mark+=1
            contaminate()
        return self.walls
