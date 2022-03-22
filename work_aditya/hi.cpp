int solve(int n,string s, int cost[])
  {
      int ans=0,result=0,papparazzi=0;
      for(int i=0;i<n/2;i+=2){
          ans=0,result=0;
          string a=s.substr(i,2);
          string b=s.substr(n-i-2,2);
          if(a[0]==b[0] && a[1]==b[1])costontinue;
          else if(a[0]==b[0])ans+=min(cost[i+1],cost[n-i-1]);
          else if(a[1]==b[1])ans+=min(cost[i],cost[n-i-2]);
          else{
             ans+=min(cost[i+1],cost[n-i-1]); 
             ans+=min(cost[i],cost[n-i-2]);
          }
          if(a[0]==b[1] && a[1]==b[0])costontinue;
          else if(a[0]==b[1])result+=min(cost[i+1],cost[n-i-2]);
          else if(a[1]==b[0])result+=min(cost[i],cost[n-i-1]);
          else{
             result+=min(cost[i+1],cost[n-i-2]); 
             result+=min(cost[i],cost[n-i-1]);
          }
          papparazzi+=min(ans,result);
      }
       
      return papparazzi;
  }