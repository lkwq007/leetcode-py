class Solution:
    def countVowels(self, word: str) -> int:
        # brute force with optim
        cnt=0
        acc=0
        ret=0
        base=0
        stack=0
        for item in word:
            if item in "aeiou":
                cnt+=1
                acc+=1
                base+=cnt
                stack+=base
                cnt=0
            else:
                cnt+=1
            ret+=stack
        return ret


class Solution:
    def countVowels(self, word: str) -> int:
        # TLE
        # brute force, no optim, TLE
        cnt=0
        acc=0
        ret=0
        stack=[]
        for item in word:
            if item in "aeiou":
                cnt+=1
                acc+=1
                stack.append(cnt)
                cnt=0
            else:
                cnt+=1
            for i in range(len(stack)):
                idx=i+1
                ret+=stack[-idx]*idx
        return ret
