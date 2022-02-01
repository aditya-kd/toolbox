def solve(self, arr, count, k):
        if len(arr) == 1:
            return arr[0]
        count = (count + k -1)%len(arr)
        arr.pop(count)
        return self.solve(arr, count, k)
def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        for i in range(1, n+1):
            arr.append(i)
            
        return self.solve(arr, 0, k)