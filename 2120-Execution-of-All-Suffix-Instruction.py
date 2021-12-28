class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # brute force
        ret=[0]*len(s)
        path=[]
        offset=[[0,1],[0,-1],[1,0],[-1,0]]
        mapping={"R":0,"L":1,"D":2,"U":3}
        for i in range(len(s)):
            acc=0
            y,x=startPos
            for j in range(i,len(s)):
                ys,xs=offset[mapping[s[j]]]
                y=y+ys
                x=x+xs
                if y<0 or y>=n or x<0 or x>=n:
                    break
                acc+=1
            ret[i]=acc
        return ret

# class Solution:
#     def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
#         # brute force
#         ret=[0]*len(s)
#         y,x=startPos
#         bbox=[y,y,x,x]
#         offset=[[0,1],[0,-1],[1,0],[-1,0]]
#         mapping={"R":0,"L":1,"D":2,"U":3}
#         for i in range(len(s)-1,-1,-1):
#             ys,xs=offset[mapping[s[i]]]
#             y+=ys
#             x+=xs
#             bbox[0]=min(bbox[0],y)
#             bbox[1]=max(bbox[1],y)
#             bbox[2]=min(bbox[2],x)
#             bbox[3]=max(bbox[3],x)
