class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        h=len(box)
        w=len(box[0])
        for y in range(h):
            last=w
            for x in range(w-1,-1,-1):
                if box[y][x]=="*":
                    last=x
                elif box[y][x]=="#":
                    box[y][x]="."
                    last-=1
                    box[y][last]="#"
        return list(zip(*(reversed(box))))