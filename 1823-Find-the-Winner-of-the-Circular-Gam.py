class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # simulation
        if k==1:
            return n
        lst=[i+1 for i in range(n)]
        cnt=k
        while len(lst)>1:
            target=[]
            for i in range(len(lst)):
                cnt-=1
                if cnt==0:
                    cnt=k
                else:
                    target.append(lst[i])
            lst=target
        return lst[0]