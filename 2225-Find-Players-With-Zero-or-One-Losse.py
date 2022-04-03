class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # You should only consider the players that have played at least one match.
        ret0=[]
        ret1=[]
        loss={}
        for w,l in matches:
            loss[w]=loss.get(w,0)
            loss[l]=loss.get(l,0)+1
        for k,v in loss.items():
            if v==0:
                ret0.append(k)
            elif v==1:
                ret1.append(k)
        ret0.sort()
        ret1.sort()
        return [ret0,ret1]