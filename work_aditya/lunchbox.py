#lex_auth_01275172151871897677


class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
            
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
            
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data
    
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    
    def get_max_size(self):
        return self.__max_size
    
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg    

#start writing your code here
class LunchBox:
    def __init__(self, color, manufacturer):
        self.__color=color
        self.__manufacturer=manufacturer
    def get_color(self):
        return self.__color
    def get_manufacturer(self):
        return self.__manufacturer
    def __str__(self):
        pass
    
class Container():
    def __init__(self, box_stack):
        self.__box_stack=box_stack
    
    def get_box_stack(self):
        return self.__box_stack

    def identify_count(self, color):
        
        temp= self.get_box_stack()
        count=0
        dic={}
        while temp.is_empty()==False:
            item= temp.pop()
            
            if (item.get_color()).lower() == color.lower():
                count=1
                dic[item.get_manufacturer()]=dic.get(item.get_manufacturer(), 0)+1
            

        
        if count==0: return 0
        # print(dic)
        return dic
            
box1= LunchBox( 'black','A' )
box2= LunchBox( 'red' ,'B'  )
box3= LunchBox( 'black' ,'C'  )
box4= LunchBox( 'red' ,'D'  )
box5= LunchBox( 'red' ,'E'  )
box6= LunchBox( 'sage green', 'F')
box7= LunchBox( 'red' ,'G'  )
box8= LunchBox( 'sage green', 'E')

s=Stack(5)
s.push(box1)
s.push(box2)
s.push(box3)
s.push(box4)
s.push(box5)

container=Container(s)
res=container.identify_count('sage green')
#res=container.identify_count('yellow')
print(res)
                

