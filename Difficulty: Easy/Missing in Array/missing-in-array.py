#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        '''for i in range(len(arr)):
            if i not in arr:    ---> inefficient check
                return i
        ''' 
        
        expected_sum = n*(n+1)//2
        
        actual_sum = sum(arr)
        
        missing_number = expected_sum - actual_sum
        
        return missing_number
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends