class Node:

    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

#actual problem
def mergeSortedList(l1, l2):

    tempNode=LinkedList()
    currNode=tempNode

    while l1!=None and l2!=None:
        if l1.data < l2.data:
            currNode.next=l1
            l1=l1.next
        else:
            currNode.next=l2
            l2=l2.next

        currNode=currNode.next

    if l1!=None:
            currNode.next=l1
            l1=l1.next

    if l2!=None:
            currNode.next=l2
            l2=l2.next
    return tempNode.next
        
            
