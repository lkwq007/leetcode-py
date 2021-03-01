class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx=0
        if ruleKey=="color":
            idx=1
        elif ruleKey=="name":
            idx=2
        ret=0
        for item in items:
            if item[idx]==ruleValue:
                ret+=1
        return ret