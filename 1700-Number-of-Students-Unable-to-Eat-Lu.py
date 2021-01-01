class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones=sum(students)
        zeros=len(students)-ones
        lst=[zeros,ones]
        for i in range(len(sandwiches)):
            item=sandwiches[i]
            if lst[item]>0:
                lst[item]-=1
            else:
                return sum(lst)
        return 0