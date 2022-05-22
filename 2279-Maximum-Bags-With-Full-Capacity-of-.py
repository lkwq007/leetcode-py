class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        lst=[capacity[i]-rocks[i] for i in range(len(rocks))]
        lst.sort()
        ret=0
        for i in range(len(lst)):
            if additionalRocks>=lst[i]:
                ret+=1
                additionalRocks-=lst[i]
            else:
                break
        return ret