from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food2rating = {}
        self.food2cusine = {}
        self.cusine2sortedfood = defaultdict(SortedSet)
        
        for i in range(len(foods)):
            self.food2rating[foods[i]] = ratings[i]
            self.food2cusine[foods[i]] = cuisines[i]
            self.cusine2sortedfood[cuisines[i]].add((-ratings[i],foods[i]))
        return     
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food2cusine[food]
        olditem = (-self.food2rating[food],food)
        self.cusine2sortedfood[cuisine].remove(olditem)
        self.cusine2sortedfood[cuisine].add((-newRating, food))       
        self.food2rating[food] = newRating
        return 
    def highestRated(self, cuisine: str) -> str:
        return self.cusine2sortedfood[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)