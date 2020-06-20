class Solution:
    def longestDupSubstring(self, S: str) -> str:
        if len(S)<2:
            return S
        term=1000000007
        base=26
        ord_a=ord("a")
        def search(s,k):
            leftmost=1
            for _ in range(1,k):
                leftmost*=base
                leftmost%=term
            record={}
            acc=0
            for idx in range(0,k):
                acc*=base
                acc+=(ord(s[idx])-ord_a)
                acc%=term
            record[acc]=[0]
            for idx in range(k,len(s)):
                acc=(acc+term-((ord(s[idx-k])-ord_a)*leftmost)%term)*base+(ord(s[idx])-ord_a)
                acc%=term
                if acc in record:
                    record[acc].append(idx-k+1)
                else:
                    record[acc]=[idx-k+1]
            for item in record:
                if len(record[item])>1:
                    idx=record[item][0]
                    ref=s[idx:idx+k]
                    for i in record[item][1:]:
                        if s[i:i+k]==ref:
                            return ref
            return ""
        left=1
        right=len(S)-1
        ret=""
        while left<=right:
            middle=left+(right-left)//2
            tmp=search(S,middle)
            if tmp:
                left=middle+1
                ret=tmp
            else:
                right=middle-1
        return ret

x=Solution()
print(x.longestDupSubstring("abcda"))