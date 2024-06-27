#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def dataTypeSize(self, str):
        # Code here
        if str[0]=='c' or str[0]=='C':
            return 1
        elif str[0]=='i' or str[0]=='I' or str[0]=='f' or str[0]=='F':
            return 4
        elif str[0]=='l' or str[0]=='L' or str[0]=='d' or str[0]=='D':
            return 8
        else:
            return -1

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
# } Driver Code Ends