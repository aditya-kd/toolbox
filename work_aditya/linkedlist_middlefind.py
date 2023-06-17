def findMidlle(head):
    slow=head
    fast=head
    if fast!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next

    return slow

# delete the middle node you need to take 
#prev pointer and store slow in that
#then prev.next=slow.next

