class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)<1 or len(matrix[0])<1:
            return []
        h=len(matrix)
        w=len(matrix[0])
        # brute force
        ret=[]
        flag=True
        y,x=0,0
        cnt=0
        total=h*w
        while cnt<total:
            cnt+=1
            ret.append(matrix[y][x])
            if flag:
                if x==w-1:
                    y+=1
                    flag=False
                elif y==0:
                    x+=1
                    flag=False
                else:
                    x+=1
                    y-=1
            else:
                if y==h-1:
                    x+=1
                    flag=True
                elif x==0:
                    y+=1
                    flag=True
                else:
                    x-=1
                    y+=1
        return ret

# class Solution:
#     def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         h=len(matrix)
#         w=len(matrix[0])
#         ret=[]
#         for i in range(h+w):
#             total=3
#             seq=reversed(range(total)) if i&1==0 else range(total)
#             for j in range(total):
#                 ret.append(matrix[j][total-j-1])
#         return ret