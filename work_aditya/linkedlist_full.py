class Node:
        def __init__(self, d):
            self.data=d
            self.next=None

class LinkedList:

    
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

    #insert at beginning
    def push_Beg(self, d):
        newnode= Node(d)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
            
    #insert at end
    def push_end(self, d):
        newnode=Node(d)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode

    #insert at position
    def push_at(self, d, p):
        newnode=Node(d)
        temp=self.head
        pos=1
        while(pos!=p):    
            temp = temp.next
            pos+=1

        newnode.next = temp.next
        temp.next=newnode
    def push_at2(self, d, p):
        p1=None
        p2=self.head
        for i in range(p-1):
            p1=p2
            p2=p2.next
        newnode=Node(d)
        p1.next=newnode
        newnode.next=p2
        

    #delete at beginning
    def delete_beg(self):
        self.head=self.head.next

    #delete at end
    def delete_end(self):
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
        
    #delet at pos
    def delete_at(self, p):
        pos=1
        temp=self.head
        while(pos!=p-1):
            temp=temp.next
            pos+=1

        temp.next=temp.next.next

        



if __name__=='__main__':
    
    ll1=LinkedList()
    
    ll1.head=Node(10)
    second=Node(20)
    third=Node(30)
    fourth=Node(40)
    ll1.head.next=second
    second.next=third
    third.next=fourth    

    print('Original List: ')
    ll1.printList()
#insert at Beginning
    ll1.push_Beg(7)
    print('After pushing at Beginnning')
    ll1.printList()
#insert at End
    ll1.push_end(89)
    print('After pushong at end')
    ll1.printList()
#insert at pos
    ll1.push_at(56, 3)
    print('After pushing at 3')
    ll1.printList()
#delete at beg
    ll1.delete_beg()
    print('After deleting from beg')
    ll1.printList()
#delete at end
    ll1.delete_end()
    print('After deleting from end')
    ll1.printList()
#delet at pos
    ll1.delete_at(3)
    print('After deleting from pos=3')
    ll1.printList()

    
    




