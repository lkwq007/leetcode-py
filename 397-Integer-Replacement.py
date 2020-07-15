class Solution:
    def integerReplacement(self, n: int) -> int:
        cnt=0
        tmp=n
        while tmp>1:
            if tmp%2==1:
                cnt+=1
            tmp=tmp>>1
            cnt+=1
        self.min=cnt
        def probe(x,cnt):
            if x==1:
                self.min=min(cnt,self.min)
                return
            if cnt>=self.min:
                return
            while x>1:
                if x%2==1:
                    cnt+=1
                    break
                x=x>>1
                cnt+=1
            if x==1:
                probe(x,cnt)
            else:
                probe(x+1,cnt)
                probe(x-1,cnt)
        probe(n,0)
        return self.min