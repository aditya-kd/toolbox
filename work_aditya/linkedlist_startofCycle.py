def startofCycle(head):
        if head==None:
            return None
        fast=head
        slow=head
        hasloop=False
        
        while fast !=None and fast.next !=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                hasloop=True
                break
                
        if fast==None or fast.next==None: return None
        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
            
        return fast