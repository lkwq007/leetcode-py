import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius=radius
        self.x=x_center
        self.y=y_center

    def randPoint(self) -> List[float]:
        pi=math.pi
        angle=2*pi*random.random()
        r=(1.0-random.random())*self.radius
        return [self.x+r*math.cos(angle),self.y+r*math.sin(angle)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()