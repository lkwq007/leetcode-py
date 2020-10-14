class Solution:
    def reorderSpaces(self, text: str) -> str:
        words=text.split()
        total=sum(map(len,words))
        if len(words)==1:
            return words[0]+" "*(len(text)-total)
        each=(len(text)-total)//(len(words)-1)
        rest=(len(text)-total)%(len(words)-1)
        space=" "*each
        ret=space.join(words)
        return ret+" "*rest