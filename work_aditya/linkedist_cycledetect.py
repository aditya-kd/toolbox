def hascycle(head):
    slow=head
    fast=head
    if head==None:
        return False
    while fast != None and fast.next != None:
        slow=slow.next
        fast=fast.next.next

        if fast==slow:
            return True

    return False
    