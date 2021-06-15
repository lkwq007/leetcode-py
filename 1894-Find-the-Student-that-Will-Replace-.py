class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # linear, we can also use binary search
        acc=0
        for i in range(len(chalk)):
            acc+=chalk[i]
            chalk[i]=acc
        rest=k%chalk[-1]
        for i in range(len(chalk)):
            if rest<chalk[i]:
                return i