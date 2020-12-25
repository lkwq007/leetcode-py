class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        lst1=[(item,False) for item in houses]
        lst2=[(item,True) for item in heaters]
        lst=lst1+lst2
        lst.sort()
        left=-2e9
        dist=[2e9]*len(houses)
        idx=0
        for pos,flag in lst:
            if flag:
                left=pos
            else:
                dist[idx]=min(dist[idx],pos-left)
                idx+=1
        idx=len(houses)-1
        right=3e9
        for pos,flag in reversed(lst):
            if flag:
                right=pos
            else:
                dist[idx]=min(dist[idx],right-pos)
                idx-=1
        return max(dist)
        
