class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        # DUMMY(HEAD)(TAIL) -> 1(0)(curr) -> 2(index) -> 3 -> NULL
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        # DUMMY(HEAD)(TAIL) -> 1(0)(curr) -> 2(index) -> 3 -> NULL
        # DUMMY(HEAD)(TAIL) -> NULL
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        # DUMMY(HEAD)(TAIL)(curr)(i) -> 1(0) -> 2(index) -> 3 -> NULL
        # DUMMY(HEAD)(TAIL)(curr.next) -> 1(0)(i)(curr) -> 2(index) -> 3 -> NULL
        while i < index and curr: #traverse a LL
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals        
