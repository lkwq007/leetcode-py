# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        template=[-1]*n
        mat=[template[:] for _ in range(m)]
        self.y=0
        self.x=0
        offset=[(0,1),(1,0),(0,-1),(-1,0)]
        self.d=0
        def move(flag):
            yo,xo=offset[self.d]
            yn=self.y+yo
            xn=self.x+xo
            if 0<=yn<m and 0<=xn<n and mat[yn][xn]==-1:
                self.y=yn
                self.x=xn
            else:
                self.d=(self.d+1)%4
                if flag:
                    move(flag)
        while head:
            val=head.val
            mat[self.y][self.x]=val
            move(head.next!=None)
            head=head.next
        return mat