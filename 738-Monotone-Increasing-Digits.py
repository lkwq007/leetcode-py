class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        lst=str(N)
        def probe(i):
            if i==len(lst):
                return ""
            cur=lst[i]
            min_rest=min(lst[i:])
            if cur<=min_rest:
                return cur+probe(i+1)
            else:
                return str(int(cur)-1)+"9"*(len(lst)-i-1)
        ret=probe(0)
        i=0
        while i<len(ret)-1 and ret[i]=="0":
            i+=1
        return int(ret[i:])
