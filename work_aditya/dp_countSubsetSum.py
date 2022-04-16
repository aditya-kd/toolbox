def countSubsetSum(wt, w, n):
    t=[[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(0, n+1):
        for j in range(0, w+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
        
    for i in range(1, n+1):
        for j in range(w+1):
            if wt[i-1]<=j:
                t[i][j]= t[i-1][j-wt[i-1]]+t[i-1][j]
            else:
                t[i][j]= t[i-1][j]
            
    return t[n][w]

def countSubsetSum2(arr, n, sm):
    t=[[0]*(sm+1)]*(n+1)
    for i in range(0, n+1):
        for j in range(0, sm+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
    
    for i in range(1, n+1):
        for j in range(1, sm+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]]+ t[i-1][j]
            else:
                t[i][j]= t[i-1][j]
    return t[n][sm]

int CountSubsetsWithSum(int arr[], int n, int sum) {
	int t[n + 1][sum + 1]; // DP - matrix
	long long m = 1e9 + 7;
	
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= sum; j++) {
			if (i == 0) 
				t[i][j] = 0;
			if (j == 0) 
				t[i][j] = 1;
		}
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= sum; j++) {
			if (arr[i - 1] <= j) 
				t[i][j] = ((t[i - 1][j - arr[i - 1]])%m + t[i - 1][j]%m)%m; 
			else
				t[i][j] = (t[i - 1][j])%m; 
		}
	}

	return t[n][sum]; 
}
ls=[2,3,5,6,8,10]
ls=[1,2,3,4,5]
ls=[3,3,3,3]
ls=[3,4,4,1]
s=10
s=10
s=0
print(countSubsetSum2(ls, s, len(ls)))
    