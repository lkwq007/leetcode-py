class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # You will buy an axis-aligned square plot of land that is centered at (0, 0).
        acc=0
        cur=0
        edge=0
        while acc<neededApples:
            edge+=2
            cur+=(edge-1)+edge+(edge-2)
            acc+=4*cur
        return edge*4