class SnapshotArray:

    def __init__(self, length: int):
        self.array=[None]*length
        self.snaps=0

    def set(self, index: int, val: int) -> None:
        if self.array[index] is None:
            if self.snaps!=0:
                self.array[index]=[[self.snaps-1,0],[self.snaps,val]]
            else:
                self.array[index]=[[self.snaps,val]]
        else:
            if self.array[index][-1][1]==val:
                self.array[index][-1][0]=self.snaps
            elif self.array[index][-1][0]==self.snaps:
                self.array[index][-1][1]=val
            else:
                self.array[index][-1][0]=self.snaps-1
                self.array[index].append([self.snaps,val])

    def snap(self) -> int:
        self.snaps+=1
        return self.snaps-1

    def get(self, index: int, snap_id: int) -> int:
        # perhaps we can use a binary search
        cache=self.array[index]
        if cache is None:
            return 0
        if snap_id>=cache[-1][0]:
            return cache[-1][1]
        left=0
        right=len(cache)-1
        while left<right:
            middle=left+(right-left)//2
            if cache[middle][0]==snap_id:
                return cache[middle][1]
            elif cache[middle][0]<snap_id:
                left=middle+1
            else:
                right=middle
        return cache[left][1]

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)