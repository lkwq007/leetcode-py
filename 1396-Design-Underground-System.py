class UndergroundSystem:

    def __init__(self):
        self.user={}
        self.station={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        enter=self.user[id]
        pair=(enter[0],stationName)
        if pair not in self.station:
            self.station[pair]=[0,0]
        self.station[pair][0]+=t-enter[1]
        self.station[pair][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        acc,total=self.station.get((startStation,endStation),(0,1))
        return acc/total            


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)