# signal=0

# def genFreq(tape,my_map):
#     for j in tape:
#         if j.lower() in my_map:
#             my_map[j.lower()]+=1
#         elif j.upper() in my_map:
#             my_map[j.upper()]+=1

# def addSpace(l, space):
#     for i in range(len(tape)-1):
#         if tape[i] ==" " and tape[i+1]==" " :
#             space+=" "
#         elif tape[i]==" " and tape[i+1]!=" ":
#             space+=" "
#             l.append(space)
#             space=""

# grammer=input()
# tape=input()
# my_map={}

# def solveforMap(my_map):
#     global signal
#     for chr in grammer:
#         if chr in my_map:
#             print("New Language Error", end="")
#             signal=1
#             break
#         my_map[chr]=0

# # genFreq(tape, my_map)
# solveforMap(my_map)
# if signal==0:
#     l=[]
#     space=""
#     addSpace(l, space)   

#     l.append("")
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
#         print('res', res,'station',station,'l[i]',l[i])
        
#     print(res,end="")

signal=0

def genFreq(tape,my_map):
    for j in tape:
        if j.lower() in my_map:
            my_map[j.lower()]+=1
        elif j.upper() in my_map:
            my_map[j.upper()]+=1

def addSpace(l, space):
    for i in range(len(tape)-1):
        if tape[i] ==" " and tape[i+1]==" ":
            space+=" "
        elif tape[i]==" " and tape[i+1]!=" ":
            space+=" "
            l.append(space)
            space=""

grammer=input()
tape=input()
my_map={}

def solveforMap(my_map):
    global signal
    for chr in grammer:
        if chr in my_map:
            print("New Language Error", end="")
            signal=1
            break
        my_map[chr]=0

# genFreq(tape, my_map)
solveforMap(my_map)
if signal==0:
    l=[]
    space=""
    addSpace(l, space)   

    l.append(" ")
    res=""
    li=tape.split()
    a=0
    
    for i in range(len(li)):
        station=""
        genFreq(li[i],my_map)
        for key,value in my_map.items():
            for z in range(value):
                station=station+key
            my_map[key]=0
        print(len(l[i]))
        res=res+station+l[i]
        
    print(res, end="")