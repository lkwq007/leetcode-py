class Fancy:

    def __init__(self):
        self.mult=1
        self.inc=0
        self.mult_lst=[]
        self.inc_lst=[]
        self.val=[]
        self.term=10**9+7

    def append(self, val: int) -> None:
        self.val.append(val)
        self.mult_lst.append(self.mult)
        self.inc_lst.append(self.inc)

    def addAll(self, inc: int) -> None:
        self.inc+=inc
        self.inc%=self.term

    def multAll(self, m: int) -> None:
        self.inc*=m
        self.mult*=m
        self.inc%=self.term
        self.mult%=self.term

    def getIndex(self, idx: int) -> int:
        # print(self.val)
        # print(self.mult,self.mult_lst)
        # print(self.inc,self.inc_lst)
        if idx>=len(self.val):
            return -1
        val=self.val[idx]
        inverse=pow(self.mult_lst[idx],-1,self.term)
        val=val*self.mult*inverse+self.inc-(self.inc_lst[idx]*self.mult*inverse)%self.term+self.term
        return val%self.term

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

class Fancy:
    # might tle
    def __init__(self):
        self.tree=[0]*(10**5*4)
        self.inc=[0]*(10**5*4)
        self.mult=[1]*(10**5*4)
        self.cnt=0
        self.term=10**9+7
        self.cur_inc=0
        self.cur_mult=1
        self.flag=False
        self.total=10**5-1
    
    def eval(self):
        if self.cnt>0 and self.flag:
            self.update(1,0,self.total,0,self.cnt-1,self.cur_inc,self.cur_mult)
        self.cur_inc=0
        self.cur_mult=1
        self.flag=False

    def push(self,v,flag=False):
        inc=self.inc[v]
        mult=self.mult[v]
        self.tree[v]=(self.tree[v]*mult+inc)%self.term
        self.inc[v]=0
        self.mult[v]=1
        if flag:
            return
        self.inc[v*2]=self.inc[v*2]*mult+inc
        self.mult[v*2]*=mult
        self.inc[v*2+1]=self.inc[v*2+1]*mult+inc
        self.mult[v*2+1]*=mult
    
    def query(self,v,tl,tr,pos):
        if tl==tr:
            self.push(v,True)
            return self.tree[v]
        else:
            self.push(v)
            tm=(tl+tr)//2
            if pos<=tm:
                return self.query(v*2,tl,tm,pos)
            else:
                return self.query(v*2+1,tm+1,tr,pos)

    def _append(self,v,tl,tr,pos,val):
        if tl==tr:
            self.tree[v]=val
        else:
            tm=(tl+tr)//2
            if pos<=tm:
                self._append(v*2,tl,tm,pos,val)
            else:
                self._append(v*2+1,tm+1,tr,pos,val)


    def update(self,v,tl,tr,l,r,inc,mult):
        if l>r:
            return
        if tl==l and tr==r:
            self.inc[v]=(self.inc[v]*mult+inc)%self.term
            self.mult[v]=(self.mult[v]*mult)%self.term
            # self.tree[v]=self.tree[v]*self.mult[v]+self.inc[v]
        else:
            self.push(v)
            tm=(tl+tr)//2
            self.update(v*2,tl,tm,l,min(r,tm),inc,mult)
            self.update(v*2+1,tm+1,tr,max(tm+1,l),r,inc,mult)
            # no need to combine

    def append(self, val: int) -> None:
        if self.flag:
            self.eval()
        self._append(1,0,self.total,self.cnt,val)
        self.cnt+=1

    def addAll(self, inc: int) -> None:
        if self.cnt>0:
            self.cur_inc+=inc
            self.flag=True

    def multAll(self, m: int) -> None:
        if self.cnt>0:
            self.cur_inc*=m
            self.cur_mult*=m
            self.flag=True

    def getIndex(self, idx: int) -> int:
        if idx>=self.cnt:
            return -1
        if self.flag:
            self.eval()
        return self.query(1,0,self.total,idx)


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)