class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
list1=ListNode(1)
list1.next=ListNode(3)
list1.next.next=ListNode(5)
list1.next.next.next=ListNode(7)

list2=ListNode(0)
list2.next=ListNode(2)
list2.next.next=ListNode(4)
list2.next.next.next=ListNode(8)
def mergeTwoLists(l1, l2):
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
        

temp=mergeTwoLists(list1, list2)
while temp:
    print(temp.val)
    temp=temp.next

    

