class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        flag=True
        for i in range(1,len(suits)):
            if suits[0]!=suits[i]:
                flag=False
                break
        if flag:
            return "Flush"
        record={}
        for item in ranks:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(key=lambda x:-record[x])
        for key in keys:
            if record[key]>=3:
                return "Three of a Kind"
            if record[key]>=2:
                return "Pair"
        return "High Card"