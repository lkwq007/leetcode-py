class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapping={}
        for item in magazine:
            if item in mapping:
                mapping[item]+=1
            else:
                mapping[item]=1
        for item in ransomNote:
            if item in mapping and mapping[item]>0:
                mapping[item]-=1
            else:
                return False
        return True