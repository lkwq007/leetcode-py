class Robot:

    def __init__(self, width: int, height: int):
        self.y=0
        self.x=0
        self.w=width
        self.h=height
        self.dir=0
        self.mapping=["East", "North", "West", "South"]

    def step(self, num: int) -> None:
        # 1 <= num <= 10^5, oh that's tedious
        lm=self.x
        rm=self.w-self.x-1
        tm=self.h-self.y-1
        bm=self.y
        if self.dir==0:
            if num<=rm:
                self.x+=num
            else:
                self.x+=rm
                self.dir+=1
                self.step(num-rm)
        elif self.dir==1:
            if num<=tm:
                self.y+=num
            else:
                self.y+=tm
                self.dir+=1
                self.step(num-tm)
        elif self.dir==2:
            if num<=lm:
                self.x-=num
            else:
                self.x-=lm
                self.dir+=1
                self.step(num-lm)
        else:
            if num<=bm:
                self.y-=num
            else:
                self.y-=bm
                self.dir=0
                self.step(num-bm)

    def getPos(self) -> List[int]:
        return [self.x,self.y]

    def getDir(self) -> str:
        return self.mapping[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()