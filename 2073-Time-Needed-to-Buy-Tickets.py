class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total=tickets[k]
        ret=0
        for i in range(len(tickets)):
            if i>k:
                ret+=min(total-1,tickets[i])
            else:
                ret+=min(total,tickets[i])
        return ret