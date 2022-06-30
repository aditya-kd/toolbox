# int maxSumAfterPartitioning(vector<int>& arr, int k) {
#         vector<int> dp(arr.size(), 0);
#         for(int i=0; i<arr.size(); i++){
#             if(i == 0){
#                 dp[i] = arr[i];
#             }
#             else{
#                 int mx = 0;
#                 for(int j = 1; j<= k; j++){
#                     if(i-j+1 >= 0){
#                         mx = max(mx, arr[i-j+1]);
#                         if(i-j >= 0){
#                             dp[i] = max(dp[i], dp[i-j] + mx * j);
#                         }
#                         else
#                             dp[i] = max(dp[i], 0 + mx * j);
#                     }
#                 }
#                 cout<<dp[i]<<" ";
#             }
#         }return dp[arr.size()-1];
#     }
# };
def solve(arr, k):
    dp=[0]*len(arr)
    for i in range(0, len(arr)):
        if i==0: dp[k]= arr[i]
    res=[]
    mx=0
    for i in range(0, len(arr)):
        for j in range(1, k+1):
            if i-j+1 >= 0:
                mx = max(mx, arr[i-j+1])
                if i-j>=0 : 
                    dp[i] = max(dp[i], dp[i-j] + mx*j)
                else:
                    dp[i] = max(dp[i], 0+mx*j)
        res.append(dp[i])

    return dp[len(arr)-1]

        

            