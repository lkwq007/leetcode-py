class Solution:
    def knightDialer(self, N: int) -> int:
        if N<2:
            return 10
        term=10**9+7
        mapping=[[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
        count=[1]*10
        for _ in range(1,N):
            target=[0]*10
            for i in range(10):
                for next in mapping[i]:
                    target[next]+=count[i]
                    target[next]%=term
            count=target
        return sum(count)%term
