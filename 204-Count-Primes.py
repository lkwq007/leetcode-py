class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        prime=[0]*n
        prime[0]=1
        prime[1]=1
        for i in range(2,n):
            if prime[i]==0 and i*i<=n:
                for j in range(i*i,n,i):
                    prime[j]=1
        return n-sum(prime)
        

class Solution:
    def countPrimes(self, n: int) -> int:
        # TLE
        if n<3:
            return 0
        lst=[2]
        cur=3
        while cur<n:
            flag=True
            for item in lst:
                if cur%item==0:
                    flag=False
                    break
                if item*item>cur:
                    break
            if flag:
                lst.append(cur)
            cur+=2
        return len(lst)