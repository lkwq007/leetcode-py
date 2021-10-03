class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # sliding windows
        # scan F
        ret=k
        start=0
        end=0
        cnt=0
        while end<len(answerKey):
            if answerKey[end]=="F":
                if cnt<k:
                    cnt+=1
                else:
                    while answerKey[start]!="F":
                        start+=1
                    start+=1
            end+=1
            ret=max(ret,end-start)
        start=0
        end=0
        cnt=0
        while end<len(answerKey):
            if answerKey[end]=="T":
                if cnt<k:
                    cnt+=1
                else:
                    while answerKey[start]!="T":
                        start+=1
                    start+=1
            end+=1
            ret=max(ret,end-start)
        return ret

