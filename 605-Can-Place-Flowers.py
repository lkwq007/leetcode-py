class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt=0
        last=-2
        for i in range(len(flowerbed)): 
            right=flowerbed[i+1] if i+1<len(flowerbed) else 0
            left=flowerbed[i-1] if i-1>=0 else 0
            if left+flowerbed[i]+right==0 and i-1!=last:
                last=i
                cnt+=1
        return cnt>=n

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt=0
        last=-2
        for i in range(len(flowerbed)): 
            right=flowerbed[i+1] if i+1<len(flowerbed) else 0
            left=flowerbed[i-1] if i-1>=0 else 0
            if left|flowerbed[i]|right==0 and i-1!=last:
                last=i
                cnt+=1
            if cnt>=n:
                return True
        return False