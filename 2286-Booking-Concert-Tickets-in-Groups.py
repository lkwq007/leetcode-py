class BookMyShow:

    def __init__(self, n: int, m: int):
        self.width=m
        self.tree=[0]*(4*n+1)
        self.mark=[False]*(4*n+1)
        self.total=n
        def build(v,tl,tr):
            if tl==tr:
                self.tree[v]=[m,m]
            else:
                mid=tl+(tr-tl)//2
                build(v*2,tl,mid)
                build(v*2+1,mid+1,tr)
                left=self.tree[v*2]
                right=self.tree[v*2+1]
                self.tree[v]=[left[0]+right[0],max(left[1],right[1])]
        build(1,0,n-1)
        print(self.tree)

    def push(self,v):
        if self.mark[v]:
            self.tree[v*2]=self.tree[v]
            self.tree[v*2+1]=self.tree[v]
            self.mark[v]=False
            self.mark[v*2]=True
            self.mark[v*2+1]=True
    
    def updateK(self,v,tl,tr,val):
        if tl==tr:
            self.tree[v][0]-=val
            self.tree[v][1]-=val
            return (tl,self.width-self.tree[v][0]-val)
        elif tl<tr:
            self.push(v)
            tm=(tl+tr)//2
            if self.tree[v*2][1]>=val:
                ret=self.updateK(v*2,tl,tm,val)
            else:
                ret=self.updateK(v*2+1,tm+1,tr,val)
            self.tree[v][0]=self.tree[v*2][0]+self.tree[v*2+1][0]
            self.tree[v][1]=max(self.tree[v*2][1],self.tree[v*2+1][1])
            return ret
        else:
            return []

    def update(self,v,tl,tr,val):
        if tl==tr:
            self.tree[v][0]-=val
            self.tree[v][1]-=val
        elif tl<tr:
            tm=(tl+tr)//2
            self.push(v)
            if self.tree[v*2][0]>=val:
                # only left
                self.update(v*2,tl,tm,val)
            else:
                rest=val-self.tree[v*2][0]
                self.tree[v*2]=[0,0]
                self.mark[v*2]=True
                self.update(v*2+1,tm+1,tr,rest)
            self.tree[v][0]=self.tree[v*2][0]+self.tree[v*2+1][0]
            self.tree[v][1]=max(self.tree[v*2][1],self.tree[v*2+1][1])
            

    def query(self,v,tl,tr,l,r):
        # print(v,tl,tr,l,r)
        if l>r:
            return [0,0]
        if tl==l and tr==r:
            return self.tree[v]
        self.push(v)
        tm=(tl+tr)//2
        left=self.query(v*2,tl,tm,l,min(tm,r))
        right=self.query(v*2+1,tm+1,tr,max(tm+1,l),r)
        return (left[0]+right[0],max(left[1],right[1]))

    def gather(self, k: int, maxRow: int) -> List[int]:
        if self.query(1,0,self.total-1,0,maxRow)[1]>=k:
            return self.updateK(1,0,self.total-1,k)
        else:
            return []

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.query(1,0,self.total-1,0,maxRow)[0]>=k:
            self.update(1,0,self.total-1,k)
            return True
        return False


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)