class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for item in asteroids:
            if item<=mass:
                mass+=item
            else:
                return False
        return True