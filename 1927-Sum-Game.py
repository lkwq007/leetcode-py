class Solution:
    def sumGame(self, num: str) -> bool:
        # even length
        left=0
        left_mark=0
        right=0
        right_mark=0
        part=len(num)//2
        for i in range(len(num)//2):
            if num[i]=="?":
                left_mark+=1
            else:
                left+=int(num[i])
            if num[i+part]=="?":
                right_mark+=1
            else:
                right+=int(num[i+part])
        if (left_mark+right_mark)%2:
            return True
        elif (left_mark+right_mark)==0:
            return left!=right
        diff=left-right
        # alice max diff
        # bob min diff
        lcnt=left_mark
        rcnt=right_mark
        if left>right:
            diff=left+(lcnt+1)//2