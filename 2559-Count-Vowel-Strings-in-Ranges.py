class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ret=[0]*len(queries)
        prefix=[0]*(len(words)+1)
        pattern=set("aeiou")
        for i,word in enumerate(words):
            prefix[i]=prefix[i-1]
            if word[0] in pattern and word[-1] in pattern:
                prefix[i]+=1
        for i,item in enumerate(queries):
            l,r=item
            ret[i]=prefix[r]-prefix[l-1]
        return ret