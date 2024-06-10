#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		order = {'!': 0, '#': 1, '$': 2, '%': 3, '&': 4, '*': 5, '?': 6, '@': 7, '^': 8}
        
        # Custom sort function based on the defined order
        def custom_sort(arr):
            return sorted(arr, key=lambda x: order[x])
        
        # Sort nuts and bolts arrays using the custom sort function
        nuts[:] = custom_sort(nuts)
        bolts[:] = custom_sort(bolts)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends