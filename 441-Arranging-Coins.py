class Solution:
    def arrangeCoins(self, n: int) -> int:
        coin=1
        total=0
        cnt=0
        while total<=n:
            total+=coin
            coin+=1
            cnt+=1
        return cnt-1

from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((sqrt(1+n<<3)-1)//2)