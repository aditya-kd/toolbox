class ListNode:
    def __init__(self, val=0):
        self.val=val
        self.next=next
    def reverse(self, head):
        curr=head
        prev=None
        next=None
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next

        return prev
        