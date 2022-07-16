class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # 0 <= n <= 10^6
        self.ret=10**7
        def check(pos,lst,acc):
            if pos==len(lst):
                if acc>n:
                    self.ret=min(self.ret,acc)
                return
            for i in range(len(lst)):
                if lst[i]!=-1:
                    x=lst[i]
                    lst[i]=-1
                    check(pos+1,lst,acc*10+x)
                    lst[i]=x
        def probe(k,acc,flag=False):
            if k==0:
                if flag:
                    val=0
                    for item in acc:
                        for i in range(item):
                            val=val*10+item
                    self.ret=min(self.ret,val)
                else:
                    lst=[]
                    for item in acc:
                        lst+=[item]*item
                    check(0,lst,0)
                return
            start=acc[-1]+1 if len(acc) else 1
            for i in range(start,7):
                if i<=k:
                    acc.append(i)
                    probe(k-i,acc)
                    acc.pop()
        probe(len(str(n)),[],False)
        if self.ret==10**7:
            probe(len(str(n))+1,[],True)
        return self.ret
            
