class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cnt=[0]*3
        self.total=[big,medium,small]
    def addCar(self, carType: int) -> bool:
        idx=carType-1
        if self.cnt[idx]<self.total[idx]:
            self.cnt[idx]+=1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)