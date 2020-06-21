from typing import List
def dump(x):
    [print(item) for item in x]
    print("")
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # perhaps we can solve this problem reverse
        if len(dungeon)<1 or len(dungeon[0])<1:
            return 0
        h=len(dungeon)
        w=len(dungeon[0])
        dungeon[-1][-1]=max(1,1-dungeon[-1][-1])
        for x in range(w-2,-1,-1):
            dungeon[-1][x]=max(1,dungeon[-1][x+1]-dungeon[-1][x])
        for y in range(h-2,-1,-1):
            dungeon[y][-1]=max(1,dungeon[y+1][-1]-dungeon[y][-1])
        for y in range(h-2,-1,-1):
            for x in range(w-2,-1,-1):
                right=max(1,dungeon[y][x+1]-dungeon[y][x])
                down=max(1,dungeon[y+1][x]-dungeon[y][x])
                dungeon[y][x]=min(right,down)
        return dungeon[0][0]

# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         # this does not lead to correct answer
#         if len(dungeon)<1 or len(dungeon[0])<1:
#             return 0
#         h=len(dungeon)
#         w=len(dungeon[0])
#         template=[0]*w
#         record=[template[:] for _ in range(h)]
#         dump(dungeon)
#         for x in range(w):
#             left=0 if x==0 else dungeon[0][x-1]
#             left_min=0 if x==0 else record[0][x-1]
#             dungeon[0][x]+=left
#             record[0][x]=min(left_min,dungeon[0][x])
#         for y in range(h):
#             top=0 if y==0 else dungeon[y-1][0]
#             top_min=0 if y==0 else record[y-1][0]
#             dungeon[y][0]+=top
#             record[y][0]=min(top_min,dungeon[y][0])
#         for y in range(1,h):
#             for x in range(1,w):
#                 left=0 if x==0 else dungeon[y][x-1]
#                 top=0 if y==0 else dungeon[y-1][x]
#                 left_min=0 if x==0 else record[y][x-1]
#                 top_min=0 if y==0 else record[y-1][x]
#                 if left_min>top_min:
#                     dungeon[y][x]+=left
#                     record[y][x]=min(left_min,dungeon[y][x])
#                 elif left_min<top_min:
#                     dungeon[y][x]+=top
#                     record[y][x]=min(top_min,dungeon[y][x])
#                 else:
#                     dungeon[y][x]+=max(left,top)
#                     record[y][x]=min(top_min,dungeon[y][x])

#         dump(dungeon)
#         dump(record)
#         return 1-record[-1][-1]

x=Solution()
print(x.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print(x.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))