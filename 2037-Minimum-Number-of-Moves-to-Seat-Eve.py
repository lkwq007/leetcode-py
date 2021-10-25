class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ret=0
        for i in range(len(seats)):
            ret+=abs(seats[i]-students[i])
        return ret