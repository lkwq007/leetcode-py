class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist=abs(target[0])+abs(target[1])
        return all(map(lambda x:x>dist,[abs(x-target[0])+abs(y-target[1]) for x,y in ghosts]))