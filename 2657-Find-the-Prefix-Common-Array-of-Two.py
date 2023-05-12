class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ret=[0]*len(A)
        setA=set()
        setB=set()
        for i in range(len(A)):
            a,b=A[i],B[i]
            ret[i]=ret[i-1]
            if a==b:
                ret[i]+=1
            if a in setB:
                ret[i]+=1
            if b in setA:
                ret[i]+=1
            setA.add(a)
            setB.add(b)
        return ret

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        lst=[0]*(len(A)+1)
        ret=[]
        acc=0
        for a,b in zip(A,B):
            lst[a]+=1
            lst[b]+=1
            if a==b:
                acc+=1
            else:
                if lst[a]==2:
                    acc+=1
                if lst[b]==2:
                    acc+=1
            ret.append(acc)
        return ret
