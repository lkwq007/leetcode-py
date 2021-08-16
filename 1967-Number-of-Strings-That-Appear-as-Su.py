class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ret=0
        for item in patterns:
            if item in word:
                ret+=1
        return ret