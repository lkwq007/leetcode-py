import heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine={}
        self.food={}
        self.food_mapping={}
        for f,c,r in zip(foods,cuisines,ratings):
            self.food[f]=r
            self.food_mapping[f]=c
            if c not in self.cuisine:
                self.cuisine[c]=[]
            heapq.heappush(self.cuisine[c],(-r,f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food[food]=newRating
        c=self.food_mapping[food]
        heapq.heappush(self.cuisine[c],(-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            top=self.cuisine[cuisine][0]
            if self.food[top[1]]==-top[0]:
                return top[1]
            heapq.heappop(self.cuisine[cuisine])
        return ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)