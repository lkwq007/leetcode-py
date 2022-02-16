class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ret=0
        record={}
        for word in words:
            rev=word[::-1]
            if record.get(rev,0)>0:
                record[rev]-=1
                ret+=4
            else:
                record[word]=record.get(word,0)+1
        for k,v in record.items():
            if v>0 and k[0]==k[1]:
                ret+=2
                break
        return ret