class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime=set([2,3,5,7,11,13,17,19])
        def count(x):
            ret=0
            while x>0:
                ret+=(x&1)
                x=x>>1
            return ret
        cnt=0
        for i in range(L,R+1):
            if count(i) in prime:
                cnt+=1
        return cnt

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime=set([2,3,5,7,11,13,17,19])
        count=[0]*(R+1)
        count[1]=1
        offset=2
        total=0
        cnt=0
        for i in range(2,R+1):
            cnt+=1
            count[i]=count[i-offset]+1
            if cnt==offset:
                offset=offset<<1
                cnt=0
            if L<=i and count[i] in prime:
                total+=1
        return total
