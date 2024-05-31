#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here 
        upper_nibble = (n >> 4) & 0x0F
        lower_nibble = n & 0x0F
        swapped = (lower_nibble << 4) | upper_nibble
        return swapped


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends