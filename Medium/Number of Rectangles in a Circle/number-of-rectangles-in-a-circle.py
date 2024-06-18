#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        count = 0
        max_side = 2 * r
        for w in range(1, max_side + 1):
            max_h = int(math.sqrt((2 * r)**2 - w**2))
            count += max_h
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends