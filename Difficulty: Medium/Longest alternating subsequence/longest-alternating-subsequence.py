#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       #code here
       if not arr:
            return 0

        # Initialize counters for up and down sequences
       up = 1
       down = 1

        # Traverse the array to update the up and down counters
       for i in range(1, len(arr)):
           if arr[i] > arr[i - 1]:
               up = down + 1
           elif arr[i] < arr[i - 1]:
               down = up + 1

        # The longest alternating sequence is the max of the two counters
       return max(up, down)


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends