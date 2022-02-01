class ListNode:
    def __init__(self,data):
        self.val=data
        self.next=None
def deleteNthNodeLast(head, n):
        dummyhead=ListNode(0)
        dummyhead.next=head
        prev=dummyhead
        curr=dummyhead
        i=0
        for i in range(1, n+2):
            curr=curr.next
            
        while curr!=None:
            
            prev=prev.next
            curr=curr.next
       
        prev.next=prev.next.next
        return dummyhead.next