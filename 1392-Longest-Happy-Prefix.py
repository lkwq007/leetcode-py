class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s)<2:
            return ""
        record={}
        
