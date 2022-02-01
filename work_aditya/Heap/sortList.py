# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(l1, l2):
        tempNode=ListNode(0)
        curNode=tempNode
        
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                curNode.next=l1
                l1=l1.next
            else:
                curNode.next=l2
                l2=l2.next
            curNode=curNode.next
        if l1!=None:
            curNode.next=l1
            l1=l1.next

        if l2!=None:
            curNode.next=l2
            l2=l2.next
        return tempNode.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:return False
        q=dequeue()
        next=None
        while head:
            q.put(head)
            prev=head
            head=head.next
            while head and prev.val <= head.val:
                prev=head
                head=head.next
            prev.next=None
            
        while len(q)>1:
            l1=q.popleft()
            l2=q.popleft()
            q.push(mergeTwoList(l1, l2))
        
        return q.popleft()
    
    