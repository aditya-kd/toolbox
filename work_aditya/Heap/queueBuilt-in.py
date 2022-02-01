from collections import deque
q=deque()
q.append('a')# add to rear []
q.append('b')
q.append('c')

print(q)
print(len(q))

print(q.popleft())
print(q.popleft())
print(q)
