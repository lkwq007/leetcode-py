class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # concatenating the first k strings in words
        acc=0
        for word in words:
            if acc+len(word)<=len(s) and s[acc:acc+len(word)]==word:
                pass
            else:
                return False
            acc+=len(word)
            if acc==len(s):
                break
        return acc==len(s)

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # brute force
        acc=""
        for word in words:
            acc+=word
            if acc==s:
                return True
        return False