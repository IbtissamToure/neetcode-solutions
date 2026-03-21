class ListNode:
    def __init__(self, val, next_node = None):
        self.val= val 
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) #dummy node to simplify deleting and adding nodes
        self.tail = self.head

    
    def get(self, index: int) -> int:
        now = self.head.next
        i = 0
        while now:
            if i == index:
                return now.val
            i+=1
            now = now.next
        return -1
                   
    def insertHead(self, val: int) -> None:
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
        now = self.head
        while i < index and now:
            i+= 1
            now = now.next
        if now and now.next:
            if now.next == self.tail:
                self.tail = now
            now.next = now.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        now = self.head.next
        vals = []
        while now:
            vals.append(now.val)
            now = now.next
        return vals
        
