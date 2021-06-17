class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        lst=range(len(triplets))
        ret=[False]*3
        for i in range(3):
            lst=filter(lambda x:triplets[x][i]<=target[i],lst)
            lst=list(lst)
        for i in range(3):
            if len(lst)==0:
                return False
            ret[i]=max(map(lambda x:triplets[x][i],lst))==target[i]
        return all(ret)