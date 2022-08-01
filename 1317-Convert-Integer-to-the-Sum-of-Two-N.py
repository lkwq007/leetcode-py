class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # brute force can work
        for i in range(1,n):
            if "0" not in str(i)+str(n-i):
                return [i,n-i]

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # can we do better?
        lst=str(n)
        if "0" not in lst and int(lst[-1])>1:
            return [1,n-1]
        last=n%10
        cut=5 if last<2 else last-1
        n-=cut
        ret=[str(cut),str(n%10)]
        def probe(val):
            if val==0:
                return
            lst=str(val)
            if "0" not in lst:
                ret[0]=lst+ret[0]
                return
            last=val%10
            if last>1:
                ret[0]="1"+ret[0]
                ret[1]=str(last-1)+ret[1]
            else:
                val-=5
                ret[0]="5"+ret[0]
                ret[1]=str(val%10)+ret[1]
            probe(val//10)
        probe(n//10)
        return [int(ret[0]),int(ret[1])]