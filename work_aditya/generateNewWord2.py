# l1,l2, k1,k2= input().lower(), input().lower(), '',''
# for i in l1:
#     if (l1.count(i)>1):
#         k=''
#         break
#     if (i in l2):
#         c= l2.count(i)
#         if (i.isalpha()):
#             k2+=i*c
#         else:
#             k1+= i*c

# print("Error") if (k1=='') else print(''.join([k2,' ',k1]), end='')

def accept(grammer, tape):
    grammer=input().lower()
    tape=input().lower()
    buffer1= ''
    buffer2= ''
    return (grammer, tape, buffer1, buffer2)
def isGrammer(grammer, tape, buffer1, buffer2):
    for i in range(len(grammer)):
        # if grammer.count(grammer[i]) > 1:
        #     temporary=''
        #     break
        if grammer[i] in tape:
            freq= tape.count(grammer[i])
            if grammer[i].isalpha()==True:
                buffer2+= grammer[i]*freq
            else:
                buffer1+= grammer[i]*freq
    if len(buffer1)==0:
        print("New Language Error", end="")
    else:
        ss=''.join([buffer2,' ',buffer1])
        print(buffer1, buffer2)
        print(ss, end="")

grmr=''
tape=''
grmr, tape, buf1, buf2=accept(grmr, tape)
isGrammer(grmr, tape,buf1, buf2)

sequence=input()
string=input()
di={}
flag=0
def dictionary(string,di):
    for j in string:
        if j.lower() in di:
            di[j.lower()]+=1
        elif j.upper() in di:
            di[j.upper()]+=1

for i in sequence:
    if i in di:
        print("New Language Error", end="")
        flag=1
        break
    di[i]=0

if flag==0:
    l=[]
    s=""
    for i in range(len(string)-1):
        if string[i] ==" " and string[i+1]==" " :
            s+=" "
        elif string[i]==" " and string[i+1]!=" ":
            s+=" "
            l.append(s)
            s=""

    l.append(" ")
    res=""
    li=string.split()
    a=0

    for i in range(len(li)):
        st=""
        dictionary(li[i],di)
        for key,value in di.items():
            for z in range(value):
                st=st+key
            di[key]=0
        
        res=res+st+l[i]
        
    print(res,end="")



# def genFreq(tape,my_map):
#     for j in tape:
#         if j.lower() in my_map:
#             my_map[j.lower()]+=1
#         elif j.upper() in my_map:
#             my_map[j.upper()]+=1
# grammer=input()
# tape=input()
# my_map={}
# signal=0

# for chr in grammer:
#     if chr in my_map:
#         print("New Language Error", end="")
#         signal=1
#         break
#     my_map[chr]=0

# if signal==0:
#     l=[]
#     space=""
#     for i in range(len(tape)-1):
#         if tape[i] ==" " and tape[i+1]==" " :
#             space+=" "
#         elif tape[i]==" " and tape[i+1]!=" ":
#             space+=" "
#             l.append(space)
#             space=""

#     l.append(" ")
#     res=""
#     li=tape.split()
#     a=0
    
#     for i in range(len(li)):
#         station=""
#         genFreq(li[i],my_map)
#         for key,value in my_map.items():
#             for z in range(value):
#                 station=station+key
#             my_map[key]=0
        
#         res=res+station+l[i]
        
#     print(res,end="")