import math
def isSetBit(num):
    k = math.log(num, 2)
    return k


def solve():
    num = int(input())
    ans = 0
    mp = {}

    for i in range(0, n):
        x = int(input())
        ele = isSetBit(x)
        mp[ele] = mp.get(ele, 0) +1

    for item in mp.keys():
        ele = mp[item]
        ans += (ele*(ele-1))//2

    print(ans)
    return ans


res1=[]
def subsequences1(s,output):
    if len(s)==0:
        # print(output)
        res1.append(output)
        return
    subsequences1(s[1:],output+s[0])
    subsequences1(s[1:],output)


def solve():
    num = str(input())
    k = int(input())
    ss = subsequences1(num, "")
    newls=[]
    for i in res1:
        if len(i)!=0:
            newls.append(int(i))
    print(newls)  
    newls.sort()


    for item in newls:
            if int(item) > k:
                return item
print(solve())


