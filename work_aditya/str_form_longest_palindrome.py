s = input()
#generating substring
ara = [s[i:j+1] for i in range(len(s)) for j in range(i,len(s))]
print(ara)
l=0
out=""
for i in ara:
	rev= i[::-1]
	if i == rev and len(i)>l:
		l=len(i)
		out=i
print(out)

