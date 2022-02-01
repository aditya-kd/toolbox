def nextSmallerElementToRight(arr, n):
	s=[]
	ans=[-1]*(n)
	for i in range(n-1, -1, -1):
		while len(s)>0 and s[-1]>=arr[i]:
			s.pop()
		if len(s)==0:
			ans[-1]=(-1)
		else:
			ans[i]=(s[-1])
		s.append(arr[i])
	return ans
	# s = []
	# v = []

	# for i in range(n - 1, -1, -1):
	# 	while(len(s) != 0 and s[-1] >= arr[i]):
	# 		s.pop()

	# 	if len(s) == 0 :
	# 		v.append(-1)

	# 	else:
	# 		v.append(s[-1])

	# 	s.append(arr[i])
	# v.reverse()
	# return v

if __name__ == '__main__':

	arr = [7, 8, 1, 4]
	ans = nextSmallerElementToRight(arr, len(arr))
	print(ans)