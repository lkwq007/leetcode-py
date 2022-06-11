from collections import deque
class MKAverage:
    # simple segment tree

    def __init__(self, m: int, k: int):
        self.tree=[(0,0)]*(10**5*4+4)
        self.m=m
        self.k=k
        self.queue=deque([],maxlen=m)
        self.total=m-k-k
    
    def update(self,v,tl,tr,pos,val):
        if tl==tr:
            cnt,acc=self.tree[v]
            self.tree[v]=(cnt+val,acc+pos*val)
        else:
            tm=(tl+tr)//2
            if pos<=tm:
                self.update(v*2,tl,tm,pos,val)
            else:
                self.update(v*2+1,tm+1,tr,pos,val)
            cnt0,acc0=self.tree[v*2]
            cnt1,acc1=self.tree[v*2+1]
            self.tree[v]=(cnt0+cnt1,acc0+acc1)

    def query(self,v,tl,tr,val):
        if tl==tr:
            return val*tl
        else:
            tm=(tl+tr)//2
            if self.tree[v*2][0]<val:
                return self.tree[v*2][1]+self.query(v*2+1,tm+1,tr,val-self.tree[v*2][0])
            else:
                return self.query(v*2,tl,tm,val)

    def addElement(self, num: int) -> None:
        if len(self.queue)==self.m:
            head=self.queue.popleft()
            self.update(1,0,10**5,head,-1)
        self.queue.append(num)
        self.update(1,0,10**5,num,1)

    def calculateMKAverage(self) -> int:
        if len(self.queue)<self.m:
            return -1
        left=self.query(1,0,10**5,self.k)
        right=self.query(1,0,10**5,self.m-self.k)
        return (right-left)//self.total


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()