class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ret=-1
        for i in range(len(words)):
            if words[i]==target:
                step=abs(startIndex-i)
                step=min(step,len(words)-step)
                if ret==-1 or ret>step:
                    ret=step
        return ret