class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # gray code
        total=2**n
        record=[0]*total
        ret=[0]*total
        ret[0]=start
        record[start]=1
        for i in range(1,total):
            mask=1
            tmp=mask^ret[i-1]
            while tmp<total:
                if record[tmp]==0:
                    ret[i]=tmp
                    record[tmp]=1
                    break
                mask=mask<<1
                tmp=mask^ret[i-1]
        return ret