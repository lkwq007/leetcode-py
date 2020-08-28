class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret=0
        while numBottles>=numExchange:
            new=numBottles//numExchange
            rest=numBottles%numExchange
            ret+=numBottles-rest
            numBottles=new+rest
        return ret+numBottles