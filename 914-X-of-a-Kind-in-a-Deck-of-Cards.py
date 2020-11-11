class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)<2:
            return False
        record={}
        for item in deck:
            record[item]=record.get(item,0)+1
        vals=list(record.values())
        x=min(vals)
        if x<2:
            return False
        for i in range(2,x):
            if all(map(lambda item:item%i==0,vals)):
                return True
        return False
        