class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        total=len(word)
        ret=0
        cnt=0
        for i in range(len(sequence)-total+1):
            if sequence[i:i+total]==word:
                cnt=1
                ret=max(cnt,ret)
                for j in range(i+total,len(sequence),total):
                    if sequence[j:j+total]==word:
                        cnt+=1
                        ret=max(cnt,ret)
                    else:
                        break
        return ret