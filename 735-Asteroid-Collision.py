from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def simulate():
            idx=0
            while idx<len(asteroids)-1:
                if not (asteroids[idx]>0 and asteroids[idx+1]<0):
                    idx+=1
                    continue
                else:
                    if abs(asteroids[idx])==abs(asteroids[idx+1]):
                        del asteroids[idx+1]
                        del asteroids[idx]
                    elif abs(asteroids[idx])>=abs(asteroids[idx+1]):
                        del asteroids[idx+1]
                    else:
                        del asteroids[idx]
            return len(asteroids)
        while len(asteroids)>1 and len(asteroids)!=simulate():
            pass
        return asteroids

def test(asteroids):
    sign=lambda x:1 if x>0 else -1
    def simulate():
        idx=0
        while idx<len(asteroids)-1:
            if not (asteroids[idx]>0 and asteroids[idx+1]<0):
                idx+=1
                continue
            else:
                if abs(asteroids[idx])==abs(asteroids[idx+1]):
                    del asteroids[idx+1]
                    del asteroids[idx]
                elif abs(asteroids[idx])>=abs(asteroids[idx+1]):
                    del asteroids[idx+1]
                else:
                    del asteroids[idx]
    def count():
        num=0
        for item in asteroids:
            num+=sign(item)
        return abs(num)
    while len(asteroids)!=count():
        simulate()
    return asteroids

test([8,-8])