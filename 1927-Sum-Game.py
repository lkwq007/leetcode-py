class Solution:
    def sumGame(self, num: str) -> bool:
        # even length
        left=0
        left_mark=0
        right=0
        right_mark=0
        part=len(num)//2
        for i in range(part):
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
        if left>right and left_mark>right_mark or (left<right and left_mark<right_mark):
            return True
        diff=max(left-right,right-left)
        mark=max(left_mark-right_mark,right_mark-left_mark)
        return diff!=(mark//2)*9