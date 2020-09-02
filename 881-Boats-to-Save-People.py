class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ret=0
        start=0
        cnt=0
        end=len(people)-1
        while cnt<len(people):
            while end>start and people[end]+people[start]>limit:
                end-=1
                ret+=1
                cnt+=1
            if start==end:
                ret+=1
                return ret
            ret+=1
            cnt+=2
            start+=1
            end-=1
        return ret
