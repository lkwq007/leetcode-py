class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # greedy
        if n==1:
            return [1]
        lst=[0]*(2*n-1)
        lst[0]=n
        lst[n]=n
        total=len(lst)
        record=[1]*(n+1)
        def probe(i,cnt):
            if cnt==total or i==total:
                return True
            for x in range(n-1,0,-1):
                offset=0 if x==1 else x
                if record[x]>0 and i+offset<total and lst[i]==0 and lst[i+offset]==0:
                    record[x]=0
                    lst[i]=x
                    lst[i+offset]=x
                    idx=i
                    while idx<total and lst[idx]>0:
                        idx+=1
                    if probe(idx,cnt+(2 if x>1 else 1)):
                        return True
                    record[x]=1
                    lst[i]=0
                    lst[i+offset]=0
            return False
        probe(1,2)
        return lst