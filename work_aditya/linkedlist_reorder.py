def findMid(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next

    return slow
    
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
        
def reorder(head):
    midN=findMid(head)
    second=reverse(midN)
        
    first=head
        
    while second.next!=None:
            temp=first.next
            first.next=second
            first=temp
            
            temp=second.next
            second.next=first
            second=temp
            
        
        
        