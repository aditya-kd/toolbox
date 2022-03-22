# c, n = [int(i) for i in input().split()]
def accept(arr):
    for i in range(n):
        id, p, a, b, k = input().split(",")
        a,b,k= int(a[2:]),int(b[2:]),int(k[2:])
        arr.append([float(p), int(id[8:]), 1, a])
        arr.append([float(p), int(id[8:]), 2, b])
        arr.append([float(p), int(id[8:]), 3, k])
        
def processSchool(l, school, threshold, pupil):
    for i in l:
        if i[1] not in pupil:
            if school[i[3]] > 0:
                school[i[3]] -= 1
                threshold[i[3]] = i[0]
                pupil.add(i[1])

def processAns(l, k, school, pupil):
    for i in l:
        if i[1] not in pupil:
            while k < len(school) and school[k][0] <= 0:
                k += 1
            if k < len(school):
                school[k][0] -= 1
                if school[k][2] == -1:
                    school[k][2] = 100
                school[k][2] = min(school[k][2], i[0])
                pupil.add(i[1])


c, n = map(int, input().split())
school = [0] + [int(i) for i in input().split()]
threshold = [-1] + [-1 for i in range(c)]
pupil = set()
l = []
accept(l)


l.sort(key=lambda x: (-x[0], x[1], x[2]))

processSchool(l, school, threshold, pupil)

school = [[school[i], i, threshold[i]] for i in range(1, len(school))]
school.sort(key=lambda x:(-x[0], x[1], x[2]))

k = 0
processAns(l, k, school, pupil)
school.sort(key=lambda x:-x[2])

for i in school:
    if i[2] != -1:
        print("C-" + str(i[1]), i[2])
    else:
        print("C-" + str(i[1]), "n/a")