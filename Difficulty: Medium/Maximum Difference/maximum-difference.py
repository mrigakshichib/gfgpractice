class Solution:
    def findMaxDiff(self, arr):
        # code here
        n = len(arr)
    
    # Initialize arrays for LS and RS
        LS = [0] * n
        RS = [0] * n
    
    # Stack for maintaining indices
        stack = []
    
    # Find LS (Nearest Smaller to Left)
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                LS[i] = arr[stack[-1]]
            else:
                LS[i] = 0
            stack.append(i)
    
    # Clear stack to reuse for RS
        stack.clear()
    
    # Find RS (Nearest Smaller to Right)
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
               stack.pop()
            if stack:
               RS[i] = arr[stack[-1]]
            else:
               RS[i] = 0
            stack.append(i)
    
    # Calculate the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(LS[i] - RS[i]))
    
        return max_diff



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends