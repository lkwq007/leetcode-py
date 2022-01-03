class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # build a loop?
        # a -> b <- c
        # a -> b -> c
        # find longest loop?
        visited=[-1]*len(favorite)
        step=0
        acc=0
        record={}
        for i in range(len(favorite)):
            if visited[i]==-1:
                x=i
                step+=1
                acc=0
                while visited[x]==-1:
                    visited[x]=(step,acc)
                    acc+=1
                    x=favorite[x]
                if visited[x][0]==step:

