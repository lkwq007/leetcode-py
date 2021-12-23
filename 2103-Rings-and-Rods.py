class Solution:
    def countPoints(self, rings: str) -> int:
        lst=[0]*10
        mapping={"R":1,"G":2,"B":4}
        for i in range(0,len(rings),2):
            c=rings[i]
            idx=int(rings[i+1])
            lst[idx]|=mapping[c]
        return sum([item==7 for item in lst])
