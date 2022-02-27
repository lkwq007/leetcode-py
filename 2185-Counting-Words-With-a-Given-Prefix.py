class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total=len(pref)
        ret=0
        for item in words:
            if item[:total]==pref:
                ret+=1
        return ret