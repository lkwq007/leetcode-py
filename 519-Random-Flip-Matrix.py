# There will be at least one free cell for each call to flip.
# At most 1000 calls will be made to flip and reset.
import random
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.total=n_rows*n_cols
        self.row=n_rows
        self.col=n_cols
        self.mapping={}

    def flip(self) -> List[int]:
        idx=random.randrange(self.total)
        if idx in self.mapping:
            new_idx=self.mapping[idx]
        else:
            new_idx=idx
        next=self.total-1
        while next in self.mapping:
            next=self.mapping[next]
        self.mapping[idx]=next
        self.total-=1
        return [new_idx%self.row,new_idx//self.row]

    def reset(self) -> None:
        self.mapping.clear()
        self.total=self.row*self.col


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()