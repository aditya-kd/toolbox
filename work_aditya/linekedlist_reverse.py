def reverse(head):
    curr=head
    prev=None
    next=None
    while curr!=None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev
#2nd approach is recursive
h=None
def revereseDriver(head):
    h=head
    revereseRecursive(None, head)
    return h
def revereseRecursive(prev, curr):
    if curr!=None:
        revereseRecursive(curr, curr.next)
        curr.next=prev
    else:
        h=prev #h is global variable

    
#Reverse in Groups of k-nodes
class ListNode:
    def __init__(self, n):
        self.val = n
        self.next= None
def reverseNode(head, k):
    n=0
    temp = head
    while temp!=None:
        temp = temp.next
        n+=1
    
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy 
    curr = head
    nextptr = None

    while n >= k:
        curr = prev.next
        nextptr = curr.next
        for i in range(1, k):
            curr.next = nextptr.next
            nextptr.next = prev.next
            prev.next = nextptr
            nextptr = curr.next

        prev = curr
        n -= k

    return dummy.next
    
