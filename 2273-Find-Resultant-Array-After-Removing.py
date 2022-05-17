class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ret=[words[0]]
        for i in range(1,len(words)):
            ref=list(sorted(list(ret[-1])))
            cur=list(sorted(list(words[i])))
            if ref==cur:
                continue
            ret.append(words[i])
        return ret