class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        pos=[]
        neg=[]
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x]>=0:
                    pos.append(matrix[y][x])
                else:
                    neg.append(matrix[y][x])
        if len(neg)%2==0:
            return sum(pos)-sum(neg)
        val=max(neg)
        if len(pos)>0:
            val=-min(min(pos),-val)
        return sum(pos)-sum(neg)+val+val

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        acc=0
        max_neg=1
        min_pos=-1
        cnt=0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x]>=0:
                    acc+=matrix[y][x]
                    if min_pos>matrix[y][x] or min_pos<0:
                        min_pos=matrix[y][x]
                else:
                    acc-=matrix[y][x]
                    cnt+=1
                    if max_neg<matrix[y][x] or max_neg>0:
                        max_neg=matrix[y][x]
        if cnt%2==0:
            return acc
        if min_pos<0:
            val=max_neg
        else:
            val=max(max_neg,-min_pos)
        return acc+val+val
