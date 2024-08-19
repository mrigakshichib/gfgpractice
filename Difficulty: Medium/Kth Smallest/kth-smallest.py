#User function Template for python3
import numpy as np
class Solution:

    def kthSmallest(self, arr,k):
        sorted_arr = np.sort(arr)
        return sorted_arr[k-1]
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends