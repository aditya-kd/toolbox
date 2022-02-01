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