class Solution:
    def repeatedCharacter(self, s: str) -> str:
        record={}
        for item in s:
            if item in record:
                return item
            record[item]=1
        return ""