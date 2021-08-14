class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival=[x/y for x,y in zip(dist,speed)]
        arrival.sort()
        for i in range(len(dist)):
            if arrival[i]<=i+1e-9:
                return i
        return len(dist)