class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # max(plants[i]) <= capacity <= 10^9
        cur=capacity
        ret=0
        for i in range(len(plants)):
            if cur<plants[i]:
                ret+=(i-1)+1+i+1
                cur=capacity-plants[i]
            else:
                ret+=1
                cur=cur-plants[i]
        return ret