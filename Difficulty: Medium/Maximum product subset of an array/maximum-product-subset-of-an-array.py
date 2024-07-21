#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        ans, maxneg, mod = 1, float('-inf'), 10**9+7
        for i in arr:
            if i != 0:
                ans *= i
            if i < 0 and maxneg < i:
                maxneg = i
        if ans < 0:
            ans //= maxneg
        ans = ans%mod
        return ans
    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends