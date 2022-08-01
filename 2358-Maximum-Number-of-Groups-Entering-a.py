class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # binary search?
        grades.sort()
        def check(x):
            last=0
            cnt=0
            acc=0
            last_cnt=0
            for i in range(len(grades)):
                acc+=len(grades)
                cnt+=1
                if acc>last and cnt>last_cnt:
                    last=acc
                    last_cnt=cnt
                    acc=0
                    cnt=0
                    x-=1
            return x<1
        left=1
        right=len(grades)
        while left<right:
            middle=left+(right-left)//2
            if not check(middle):
                right=middle
            else:
                left=middle+1
        while not check(left):
            left-=1
        return left
