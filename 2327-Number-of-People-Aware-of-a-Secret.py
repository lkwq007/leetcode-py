class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        known=[0]*(n+n)
        infect=[0]*(n+n)
        known[0]=1
        known[forget]=-1
        infect[delay]=1
        infect[forget]=-1
        acc=0
        term=10**9+7
        for i in range(1,n):
            infect[i]+=infect[i-1]
            known[i]+=infect[i]+known[i-1]
            known[i+forget]-=infect[i]
            infect[i+delay]+=infect[i]
            infect[i+forget]-=infect[i]
        return known[n-1]%term