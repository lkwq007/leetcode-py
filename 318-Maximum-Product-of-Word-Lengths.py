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

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # pruning
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
        words.sort(key=lambda x:-len(x))
        word_masks=[convert(item) for item in words]
        ret=0
        for i in range(len(words)):
            if len(words[i])*len(words[i])<=ret: # the rest will not be counted
                return ret
            for j in range(i+1,len(words)):
                if word_masks[i]&word_masks[j]==0:
                    ret=max(ret,len(words[i])*len(words[j]))
                    # the rest is less than ret
                    break
        return ret