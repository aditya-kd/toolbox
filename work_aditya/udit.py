def findSubarrCnt(arr, n) :
 ans = 0 
 XOR = 0
 prefix = [0] * n
 for i in range(n) :
 
  XOR = XOR ^ arr[i]
  prefix[i] = XOR

 oddGroup = dict.fromkeys(prefix, 0)
 evenGroup = dict.fromkeys(prefix, 0)
 oddGroup[0] = 1

 for i in range(n) :

  if (i & 1) :
   ans += oddGroup[prefix[i]]
   oddGroup[prefix[i]] += 1
  else :
   ans += evenGroup[prefix[i]]
   evenGroup[prefix[i]] += 1
   
   
 return ans