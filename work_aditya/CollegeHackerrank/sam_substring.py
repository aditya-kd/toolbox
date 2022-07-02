def substring2(str, n):
    total=0
    for i in range(len(str)):
        temp=''
        for j in range(i,n):
            temp+=(str[j])
            print(temp)
            total+=int(temp)
    return total

# */
# const int md=1000000007;
# int substrings(string s) {
# int n = s.size();
# vector<long> a(n), b(n);
#     a[0]=1, b[0]=1;
#     for(int i=1;i<n;i++)
#     {
#         a[i]= (10*a[i-1])%md;
#         b[i]= (b[i-1]+ a[i])%md;
#     }
#     long ans=0;
#     for(int i=0;i<n;i++)
#     {
#         ans+= ((s[i]-'0')*b[n-i-1]*(i+1))%md;
#         ans%= md;
#     }
#     return ans;
# }
s='1234'
n=len(s)
print(substring2(s,n))