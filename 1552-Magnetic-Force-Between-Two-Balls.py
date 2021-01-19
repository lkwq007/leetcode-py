class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m<3:
            return position[-1]-position[0]
        self.ret=len(position)
        def search(left,right):
            l=left
            r=right
            while left<right:
                middle=left+(right-left)//2
                if position[middle]-position[left]>=position[middle+1]-position[left]:
                    left=middle+1
                else:
                    right=middle
            self.ret=min(self.ret,position[middle]-position[l],position[r]-position[middle])