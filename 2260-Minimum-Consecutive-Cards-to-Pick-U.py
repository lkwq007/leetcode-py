class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ret=-1
        record={}
        for i in range(len(cards)):
            item=cards[i]
            if item in record:
                cur=i-record[item]+1
                if ret==-1 or ret>cur:
                    ret=cur
            record[item]=i
        return ret