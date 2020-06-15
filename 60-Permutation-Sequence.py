class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        base=ord("0")
        def to_str(num):
            return chr(base+num)
        factorial=[1]*10
        idx=1
        while idx<10:
            factorial[idx]=idx*factorial[idx-1]
            idx+=1
        tmp=n
        ret=""
        template=[to_str(x) for x in range(1,n+1)]
        k-=1
        while tmp>0:
            term=factorial[tmp-1]
            digit=k//term
            ret+=template[digit]
            del template[digit]
            k=k%term
            tmp-=1
        return ret
x=Solution()
print(x.getPermutation(3,2))