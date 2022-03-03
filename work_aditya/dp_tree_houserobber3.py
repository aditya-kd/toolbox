def g(root, dp):
    if root==None:
        return 0
    return f(root.left, dp)+f(root.right, dp)
def f(root, dp):
    if root==None: return dp[root]
    if dp[root]>0: return dp[root]

    without= f(root.left, dp) + f(root.right, dp)
    withed= root.val+ g(root.left, dp) + g(root.right, dp)
    dp[root] = max(without, withed)
    return dp[root]