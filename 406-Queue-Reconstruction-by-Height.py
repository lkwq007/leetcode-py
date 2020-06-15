class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people)<1:
            return people
        ret=[None]*len(people)
        people.sort(key=lambda x: -x[1])
        people.sort(key=lambda x: x[0])
        idx_lst=list(range(0,len(people)))
        for h,k in people:
            idx=idx_lst.pop(k)
            ret[idx]=[h,k]
        return ret
