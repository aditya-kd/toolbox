def mergeIntervals(arr):
        
        arr.sort(key = lambda x: x[0])
        ans = []
        start = -10000
        end = -100000
        for i in range(len(arr)):
            interval = arr[i]
            if interval[0] > end:
                if i != 0:
                    ans.append([start,end])
                end = interval[1]
                start = interval[0]
            else:
                if interval[1] >= end:
                    end = interval[1]
 
        if end != -100000 and [start, end] not in ans:
            ans.append([start, end])
        print(ans)
        return ans
        # print("The Merged Intervals are :", end = " ")
        # for i in range(len(m)):
        #     print(m[i], end = " ")

arr = [ [1, 9], [2, 4], [4, 7], [6, 8]]
# arr= [[1,3],[2,6],[8,10],[15,18]]
mergeIntervals(arr)

