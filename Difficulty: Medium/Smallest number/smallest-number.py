#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        # code here
        if s > 9 * d:
            return "-1"

    # Initialize result with all zeros
        result = [0] * d

    # Start from the last position
        for i in range(d - 1, -1, -1):
            if s > 9:
                result[i] = 9
                s -= 9
            else:
                result[i] = s
                s = 0

    # If the first digit is zero, adjust it
        if result[0] == 0:
            result[0] = 1
            for i in range(1, d):
                if result[i] > 0:
                    result[i] -= 1
                    break
    
    # Convert result to string
        return ''.join(map(str, result))


#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends