class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        lst=[i for i,item in enumerate(restaurants,0) if item[2]>=veganFriendly and item[3]<=maxPrice and item[4]<=maxDistance]
        lst.sort(key=lambda x:(-restaurants[x][1],-restaurants[x][0]))
        return [restaurants[i][0] for i in lst]