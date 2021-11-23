class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        self.ret=-1 if len(A) else 0
        record={}
        disjoint=[-1]*len(A)
        def find(x):
            idx=x
            while disjoint[idx]>=0:
                idx=disjoint[idx]
            while disjoint[x]>=0:
                tmp=disjoint[x]
                disjoint[x]=idx
                x=tmp
            return idx
        def union(a,b):
            if a==b:
                return
            a_idx=find(a)
            b_idx=find(b)
            if a_idx==b_idx:
                return
            disjoint[a_idx]+=disjoint[b_idx]
            disjoint[b_idx]=a_idx
            self.ret=min(self.ret,disjoint[a_idx])
        def factor(x,idx):
            if x%2==0:
                union(record.get(2,idx),idx)
                record[2]=idx
                while x%2==0:
                    x=x//2
            i=3
            while i*i<=x:
                if x%i==0:
                    union(record.get(i,idx),idx)
                    record[i]=idx
                while x%i==0:
                    x=x//i
                i+=2
            if x>1:
                union(record.get(x,idx),idx)
                record[x]=idx
        for i,item in enumerate(A,0):
            factor(item,i)
        return -self.ret

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        self.ret=0
        record={}
        disjoint=[-1]*len(A)
        def find(x):
            idx=x
            while disjoint[idx]>=0:
                idx=disjoint[idx]
            while disjoint[x]>=0:
                tmp=disjoint[x]
                disjoint[x]=idx
                x=tmp
            return idx
        def union(a,b):
            if a==b:
                return
            a_idx=find(a)
            b_idx=find(b)
            if a_idx==b_idx:
                return
            disjoint[a_idx]+=disjoint[b_idx]
            disjoint[b_idx]=a_idx
            self.ret=min(self.ret,disjoint[a_idx])
        def factor(x,idx):
            if x<3:
                union(record.get(x,idx),idx)
                record[x]=idx
                return
            if x%2==0:
                union(record.get(2,idx),idx)
                record[2]=idx
                while x%2==0:
                    x=x//2
            i=3
            while i*i<=x:
                if x%i==0:
                    union(record.get(i,idx),idx)
                    record[i]=idx
                while x%i==0:
                    x=x//i
                i+=2
            if x>1:
                union(record.get(x,idx),idx)
                record[x]=idx
        factors=[factor(A[i],i) for i in range(len(A))]
        return -self.ret

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # a brute force method
        self.ret=0
        record={}
        def factor(x,idx):
            if x<3:
                record[x]=idx
                return set([x])
            ret=set([])
            if x%2==0:
                ret.add(2)
                record[2]=idx
                while x%2==0:
                    x=x//2
            i=3
            while i*i<=x:
                if x%i==0:
                    record[i]=idx
                    ret.add(i)
                while x%i==0:
                    x=x//i
                i+=2
            if x>1:
                ret.add(x)
                record[x]=idx
            return ret
        disjoint=[-1]*len(A)
        factors=[factor(A[i],i) for i in range(len(A))]
        keys=sorted(list(record.keys()))
        def find(x):
            idx=x
            while disjoint[idx]>=0:
                idx=disjoint[idx]
            while disjoint[x]>=0:
                tmp=disjoint[x]
                disjoint[x]=idx
                x=tmp
            return idx
        def union(a,b):
            if a==b:
                return
            a_idx=find(a)
            b_idx=find(b)
            if a_idx==b_idx:
                return
            disjoint[a_idx]+=disjoint[b_idx]
            disjoint[b_idx]=a_idx
            self.ret=min(self.ret,disjoint[a_idx])
        for key in keys:
            for i in range(len(A)):
                if key in factors[i]:
                    union(record[key],i)
        return -self.ret

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # a brute force method
        self.ret=0
        def factor(x):
            if x<3:
                return set([x])
            i=2
            ret=set([])
            while i<=x:
                if x%i==0:
                    ret.add(i)
                while x%i==0:
                    x=x//i
                i+=1
            return ret
        disjoint=[-1]*len(A)
        factors=[factor(item) for item in A]
        def find(x):
            idx=x
            while disjoint[idx]>=0:
                idx=disjoint[idx]
            while disjoint[x]>=0:
                tmp=disjoint[x]
                disjoint[x]=idx
                x=tmp
            return idx
        def union(a,b):
            a_idx=find(a)
            b_idx=find(b)
            if a_idx==b_idx:
                return
            if factors[a_idx].intersection(factors[b_idx]):
                disjoint[a_idx]+=disjoint[b_idx]
                disjoint[b_idx]=a_idx
                factors[a_idx]=factors[a_idx].union(factors[b_idx])
                self.ret=min(self.ret,disjoint[a_idx])
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                union(i,j)
        return -self.ret

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # a brute force method
        self.ret=0
        disjoint=[-1]*len(A)
        def find(x):
            idx=x
            while disjoint[idx]>=0:
                idx=disjoint[idx]
            while disjoint[x]>=0:
                tmp=disjoint[x]
                disjoint[x]=idx
                x=tmp
            return idx
        def union(a,b):
            a_idx=find(a)
            b_idx=find(b)
            if a_idx==b_idx:
                return
            disjoint[a_idx]+=disjoint[b_idx]
            disjoint[b_idx]=a_idx
            self.ret=min(self.ret,disjoint[a_idx])
        def gcd(a,b):
            if a==b:
                return a
            elif a>b:
                return gcd(a-b,b)
            else:
                return gcd(a,b-a)
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i]%2==0 and A[j]%2==0 or gcd(A[i],A[j])>1:
                    union(i,j)
        return -self.ret

