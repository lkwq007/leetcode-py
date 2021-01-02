class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret=[]
        h=len(matrix)
        w=len(matrix[0])
        def move(y,x,offset):
            if x==w-offset-1 and y<h-offset-1:
                y+=1
            elif y==h-offset-1 and x>offset:
                x-=1
            elif x==offset and y>offset:
                y-=1
            elif y==offset and x<w-offset-1:
                x+=1
            # print(y,x)
            return y,x
        # can be done with DFS / or offset
        for offset in range((min(h,w)+1)//2):
            # print(offset,w-offset-1,h-offset-1)
            y0,x0=offset,offset
            ret.append(matrix[y0][x0])
            if y0==h-offset-1 and x0==w-offset-1:
                break
            if y0==h-offset-1:
                for x in range(offset+1,w-offset):
                    ret.append(matrix[y0][x])
                break
            if x0==w-offset-1:
                for y in range(offset+1,h-offset):
                    ret.append(matrix[y][x0])
                break
            y,x=move(y0,x0,offset)
            while not (y==y0 and x==x0):
                ret.append(matrix[y][x])
                y,x=move(y,x,offset)
        return ret