class ListNode:
    def __init__(self, val):
        self.val=val
        self.next=None
    
def partition(head, x):
            
        small=ListNode(0,None)
        small_head=small
        large=ListNode(0, None)
        large_head=large
        
        while head!=None:
            if head.val< x:
                small_head.next=head
                small_head = small_head.next
            else:
                large_head.next= head
                large_head = large_head.next
            
            head = head.next
            
        large_head.next = None
        small_head.next = large.next
        return small.next
    