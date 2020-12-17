class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ret=len(words)
        for word in words:
            for item in word:
                if item not in allowed:
                    ret-=1
                    break
        return ret