# from threading import get_ident


# t=int(input())
# row,col,tower=map(int, input().split())
# width=[0]
# height=[0]
# for i in range(tower):
#     c, r= map(int, input().split())
#     width.append(c)
#     height.append(r)

# width.append(row+1)
# height.append(col+1)
# width.sort()
# height.sort()

# for i in range(len(width)-1):
#     tower


def findPenalty(w, h, n, towers):
    width=[0]
    height=[0]
    for tower in towers:
        width.append(tower[0])
        height.append(tower[1])
    width.append(w+1)
    height.append(h+1)
    width.sort()
    height.sort()
    max_height=0
    max_width=0
    for i in range(n+1):
        max_width = max(max_width, width[i+1]- width[i]-1)
        max_height= max(max_height, height[i+1]- height[i]-1)

    return max_height*max_width
    



