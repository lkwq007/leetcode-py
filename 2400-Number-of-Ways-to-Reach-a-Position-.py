class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        offset=abs(endPos-startPos)
        diff=k-offset
        if k<offset or diff%2==1:
            return 0
        term=10**9+7
        forward=k+diff//2
        backward=diff//2
        def probe(n,k):
            