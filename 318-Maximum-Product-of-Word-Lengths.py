class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask=1
        mapping={}
        for i in range(ord("a"),ord("z")+1):
            mapping[chr(i)]=mask
            mask=mask<<1
        def convert(word):
            ret=0
            for item in word:
                ret|=mapping[item]
            return ret
        word_masks=[convert(item) for item in words]
        ret=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if word_masks[i]&word_masks[j]==0:
                    ret=max(ret,len(words[i])*len(words[j]))
        return ret