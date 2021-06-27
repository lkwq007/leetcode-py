class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        if len(A)<2:
            return False
        total=sum(A)
        n=len(A)
        import functools
        @functools.lru_cache(maxsize=None)
        def check(target,idx,k):
            if k==0:
                return target==0
            if n-idx<k or idx>=n or target<0:
                return False
            return check(target-A[idx],idx+1,k-1) or check(target,idx+1,k)
        for i in range(1,(n+1)//2+1):
            if (i*total)%n==0 and check(total*i//n,0,i):
                return True
        return False

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        # avg_a = avg_b , avg_a * k + avg_b * (n-k) = total, avg * n = total
        # sum / k * n == total, sum * n == total * k, sum = total * k // n
        if len(A)<2:
            return False
        total=sum(A)
        n=len(A)
        dp={0:set([0])}
        mapping={}
        mask=1
        for i in range(len(A)):
            mapping[i]=mask
            mask=mask<<1
        for k in range(1,(n+1)//2+1):
            target={}
            for key,val in dp.items():
                for v in val:
                    for i in range(len(A)):
                        if mapping[i]&v==0:
                            next=A[i]+key
                            if next not in target:
                                target[next]=set([])
                            target[next].add(mapping[i]|v)
            dp=target
            if (total*k)%n==0 and (total*k)//n in target:
                return True
        return False
                
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        # avg_a = avg_b , avg_a * k + avg_b * (n-k) = total, avg * n = total
        # sum / k * n == total, sum * n == total * k, sum = total * k // n
        if len(A)<2:
            return False
        total=sum(A)
        n=len(A)
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(k,mask):
            cur=1
            cnt=0
            acc=0
            for i in range(len(A)):
                if mask&cur:
                    cnt+=1
                    acc+=A[i]
                cur=cur<<1
            if cnt==k:
                return acc*n==total*cnt
            if acc*n>=total*k:
                return False
            cur=1
            for i in range(len(A)):
                if mask&cur==0:
                    if probe(k,mask|cur):
                        return True
                cur=cur<<1
            return False
        for k in range(1,(n+1)//2+1):
            if (total*k)%n==0:
                if probe(k,0):
                    return True
        return False



class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        import functools
        total=sum(A)
        @functools.lru_cache(maxsize=None)
        def probe(mask):
            cur=1
            cnt=0
            acc=0
            for i in range(len(A)):
                if mask&cur:
                    cnt+=1
                    acc+=A[i]
                cur=cur<<1
            if cnt==(len(A)+1)//2:
                return False
            cur=1
            for i in range(len(A)):
                if mask&cur:
                    pass
                else:
                    if (acc+A[i])*(len(A)-cnt-1)==(total-acc-A[i])*(cnt+1) or probe(mask|cur):
                        return True
                cur=cur<<1
            return False
        return probe(0)