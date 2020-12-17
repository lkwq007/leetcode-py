class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        h=len(nums)
        w=len(nums[0])
        if h*w!=r*c:
            return nums
        template=[0]*c
        ret=[template[:] for _ in range(r)]
        i=0
        j=0
        for y in range(r):
            for x in range(c):
                ret[y][x]=nums[i][j]
                j+=1
                if j==w:
                    i+=1
                    j=0
        return ret