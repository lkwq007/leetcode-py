class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        left=[-1]*len(parents)
        right=[-1]*len(parents)
        total=len(parents)
        ret=0
        max_val=total-1
        for i in range(1,len(parents)):
            item=parents[i]
            if left[item]==-1:
                left[item]=i
            else:
                right[item]=i
        for i in range(len(parents)):
            if left[i]==-1 and right[i]==-1:
                
