def conflict(board):
    n = len(board)
    if n==1:
        return 0

    row_frequency = [0] * n
    main_diag_frequency = [0] * (2 * n)
    secondary_diag_frequency = [0] * (2 * n)

    for i in range(n):
        row_frequency[board[i]] += 1
        main_diag_frequency[board[i] + i] += 1
        secondary_diag_frequency[n - board[i] + i] += 1

    conflicts = 0
    for i in range(2*n):
        if i < n:
            conflicts += (row_frequency[i] * (row_frequency[i]-1)) / 2

        conflicts += (main_diag_frequency[i] * (main_diag_frequency[i]-1)) / 2
        conflicts += (secondary_diag_frequency[i]* (secondary_diag_frequency[i]-1)) / 2
    return int(conflicts)

n=int(input())
m=int(input())
ls=[]
for i in range(m):
    a,b=map(int,input().split())
    ls.append(b)
print(conflict(ls))