class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 1 <= s1.length <= 30
        if sorted(s1)!=sorted(s2):
            return False
        if len(s1)<3:
            return True
        base=ord("a")
        import functools
        @functools.lru_cache(None)
        def check(a,b):
            if a==b:
                return True
            cnt=[0]*26
            for i in range(len(a)):
                c1=ord(a[i])-base
                cnt[c1]+=1
            acc1=[0]*26
            acc2=[0]*26
            rest=[0]*26
            for i in range(len(a)-1):
                c1=ord(a[i])-base
                c2=ord(b[i])-base
                c3=ord(a[len(a)-i-1])-base
                acc1[c1]+=1
                acc2[c2]+=1
                rest[c3]+=1
                if acc1==acc2 and check(a[:i+1],b[:i+1]) and check(a[i+1:],b[i+1:]):
                    return True
                if acc2==rest and check(a[len(a)-i-1:],b[:i+1]) and check(a[:len(a)-i-1],b[i+1:]):
                    return True
            return False
        return check(s1,s2)
