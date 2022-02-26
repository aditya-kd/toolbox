class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKSortedLists(lists):
    if lists==None or len(lists)==0:
        return None
    while len(lists)>1:
        merged=[]

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            if i+1<len(lists):
                l2=lists[i+1]
            else:
                l2=None
            merged.append(merge2Lists(l1,l2))
        lists=merged
    return lists[0]

def merge2Lists(l1, l2):
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