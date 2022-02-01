from multiprocessing import dummy


class ListNode:
    def __init__(self, val=0):
        self.val=val
        self.next=None
def addTwoNumbers(l1, l2):
    dummyHead=ListNode()
    curr=dummyHead
    p=l1
    q=l2
    c=0
    while p!=None or q!=None:
        x= p.val if p!=None else 0
        y= q.val if q!=None else 0
        sum= c+x+y
        c=sum//10
        curVal=sum%10
        
        curr.next= ListNode(curVal)
        curr=curr.next
        if q!=None:
            q=q.next
        if p!=None:
            p=p.next
    if c>0:
        curr.next=ListNode(c)
    return dummyHead.next