class Node:
    def __init__(self) -> None:
        self.prev=None
        self.next=None
        self.body=""
        self.len=0

class TextEditor:

    def __init__(self):
        head=Node()
        self.head=head
        self.ptr=self.head
        self.inner=0

    def addText(self, text: str) -> None:
        if self.inner!=len(self.ptr.body):
            tail=self.ptr.body[self.inner:]
            node=Node()
            node.body=tail
            node.next=self.ptr.next
            if node.next is not None:
                node.next.prev=node
            node.prev=self.ptr
            self.ptr.next=node
        head=self.ptr.body[:self.inner]
        self.ptr.body=head+text
        self.inner+=len(text)


    def deleteText(self, k: int) -> int:
        ret=0
        while self.ptr.prev:
            if self.inner>=k:
                head=self.ptr.body[:self.inner-k]
                tail=self.ptr.body[self.inner:]
                self.ptr.body=head+tail
                self.inner=self.inner-k
                ret+=k
                k=0
                break
            else:
                self.ptr.body=self.ptr.body[self.inner:]
                k-=self.inner
                ret+=self.inner
                prev=self.ptr.prev
                if len(self.ptr.body)==0:
                    prev.next=self.ptr.next
                    if self.ptr.next is not None:
                        self.ptr.next.prev=prev
                self.ptr=prev
                self.inner=len(self.ptr.body)
        if k>0:
            if self.inner>=k:
                head=self.ptr.body[:self.inner-k]
                tail=self.ptr.body[self.inner:]
                self.ptr.body=head+tail
                self.inner=self.inner-k
                ret+=k
            else:
                self.ptr.body=self.ptr.body[self.inner:]
                k-=self.inner
                ret+=self.inner
                self.inner=0
        return ret

    def peak(self):
        ret=""
        ptr=self.ptr
        acc=10
        cursor=self.inner
        while ptr:
            if cursor>=acc:
                ret=ptr.body[cursor-acc:cursor]+ret
                acc=0
                break
            else:
                ret=ptr.body[:cursor]+ret
                acc-=cursor
            ptr=ptr.prev
            if ptr:
                cursor=len(ptr.body)
        return ret

    def cursorLeft(self, k: int) -> str:
        while self.ptr.prev:
            if self.inner>=k:
                self.inner-=k
                k=0
                break
            else:
                k-=self.inner
                self.ptr=self.ptr.prev
                self.inner=len(self.ptr.body)
        if k>0:
            if self.inner>=k:
                self.inner-=k
            else:
                self.inner=0
                return ""
        return self.peak()

    def cursorRight(self, k: int) -> str:
        while self.ptr.next:
            if len(self.ptr.body)-self.inner>=k:
                self.inner+=k
                k=0
                break
            else:
                k-=len(self.ptr.body)-self.inner
                self.inner=0
                self.ptr=self.ptr.next
        if k>0:
            if len(self.ptr.body)-self.inner>=k:
                self.inner+=k
            else:
                self.inner=len(self.ptr.body)
        return self.peak()
                


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)