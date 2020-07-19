class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n<1:
            return [0]
        # flip one bit each time
        ret=[0]*(2**n)
        total=2**n
        record={0:1}
        masks=[0]*n
        mask=1
        for i in range(n):
            masks[i]=mask
            mask=mask<<1
        def probe(cur,pos):
            if pos==total:
                return True
            for i in range(n):
                tmp=cur^masks[i]
                if tmp not in record or record[tmp]==0:
                    ret[pos]=tmp
                    record[tmp]=1
                    if probe(tmp,pos+1):
                        return True
                    record[tmp]=0
            return False
        probe(0,1)
        return ret