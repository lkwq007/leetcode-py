class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        total=N
        for idx in range(1,L):
            if K>0:
                K-=1
                N-=1
            total*=(N-1)
        return total