class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # brute force
        total=len(part)
        idx=total
        while idx<=len(s):
            if s[(idx-total):idx]==part:
                s=s[:(idx-total)]+s[idx:]
                idx=max(total,idx-total)
            else:
                idx+=1
        return s