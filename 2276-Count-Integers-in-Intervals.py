class CountIntervals:

    def __init__(self):
        self.tree=[[0,-1,-1,False]]
    
    def update(self,v,tl,tr,l,r):
        if l>r:
            return v
        if v<0:
            v=len(self.tree)
            self.tree.append([0,-1,-1,False])
        if l==tl and r==tr:
            self.tree[v][0]=r-l+1
            self.tree[v][-1]=True
        elif not self.tree[v][-1]:
            tm=(tl+tr)//2
            self.tree[v][1]=self.update(self.tree[v][1],tl,tm,l,min(r,tm))
            self.tree[v][2]=self.update(self.tree[v][2],tm+1,tr,max(l,tm+1),r)
            vl=self.tree[v][1]
            vr=self.tree[v][2]
            left=0 if vl<0 else self.tree[vl][0]
            right=0 if vr<0 else self.tree[vr][0]
            lflag=False if vl<0 else self.tree[vl][-1]
            rflag=False if vr<0 else self.tree[vr][-1]
            self.tree[v][0]=left+right
            self.tree[v][-1]=lflag and rflag
        # print(v,tl,tr,l,r,self.tree[v])
        return v

    def add(self, left: int, right: int) -> None:
        self.update(0,0,10**9-1,left-1,right-1)

    def count(self) -> int:
        return self.tree[0][0]


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()