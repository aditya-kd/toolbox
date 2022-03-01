def getTopView(head, dis, level, dict):
    if head==None:
        return 
    if dis not in dict or level < dict[dis][1]:
        dict[dis]=(head.info, level)
    getTopView(head.left, dis-1, level+1 ,dict)
    getTopView(head.right, dis+1, level+1, dict)

def topView(root):
    #Write your code here
    dict={}
    getTopView(root, 0,0,dict)
    for key in sorted(dict.keys()):
        print(dict.get(key)[0], end=' ')
    