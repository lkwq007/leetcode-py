class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt=0
        total=0
        for i in range(len(flowerbed)):
            