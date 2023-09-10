class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        for c,word in zip(s,words):
            if c!=word[0]:
                return False
        return True
