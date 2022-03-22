from itertools import chain, combinations

def power(iterable) :
  s = list(iterable)
  return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

n = int(input())
match = input().split(",")
string = input().split(",")

subsets = list(power(string))

for i,j in enumerate(subsets) :
  if list(j) == match :
    print(i+1)
    break