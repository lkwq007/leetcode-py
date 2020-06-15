class Solution:
    def countBits(self, num: int) -> List[int]:
        ret=[0]*(num+1)
        for idx in range(0,num+1):
            ret[idx]=ret[idx>>1]+idx%2
        return ret
class Solution:
    def countBits(self, num: int) -> List[int]:
        ret=[0]*(num+1)
        for idx in range(0,num+1):
            ret[idx]=ret[idx-1] if idx%2 else ret[idx>>1]
        return ret
class Solution:
    def countBits(self, num: int) -> List[int]:
        ret=[0]*(num+1)
        if num<1:
            return ret
        ret[1]=1
        pos=2
        for idx in range(2,num+1):
            if pos<=idx<2*pos:
                ret[idx]=1+ret[idx-pos]
            else:
                pos=2*pos
                ret[idx]=1
        return ret
class Solution:
    def countBits(self, num: int) -> List[int]:
        def count(n):
            cnt=0
            while n>0:
                if n&1==1:
                    cnt+=1
                n=n>>1
            return cnt
        ret=[0]*(num+1)
        for idx in range(1,num+1):
            ret[idx]=count(idx)
        return ret