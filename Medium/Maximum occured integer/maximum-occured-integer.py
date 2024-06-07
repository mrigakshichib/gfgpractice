#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        ##Your code here
        freq = [0] * (maxx + 2)
        
        # Step 2: Mark the start and end of each range
        for i in range(n):
            freq[l[i]] += 1
            if r[i] + 1 <= maxx:
                freq[r[i] + 1] -= 1
        
        # Step 3: Compute the prefix sum to get the actual frequency
        max_occurrence = 0
        max_index = 0
        current_frequency = 0
        
        for i in range(maxx + 1):
            current_frequency += freq[i]
            if current_frequency > max_occurrence:
                max_occurrence = current_frequency
                max_index = i
        
        return max_index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends