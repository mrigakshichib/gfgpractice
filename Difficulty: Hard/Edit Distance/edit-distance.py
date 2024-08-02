class Solution:
	def editDistance(self, str1, str3):
		# Code here
		n = len(str1)
        m = len(str3)
        dp = {}
        def solve(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if str1[i]==str3[j]:
                return 0+solve(i-1,j-1)
            
            insert = 1+solve(i,j-1)
            delete = 1+ solve(i-1,j)
            replace = 1+ solve(i-1,j-1)
            dp[(i,j)] = min(insert,delete,replace)
            return dp[(i,j)]
        return solve(n-1,m-1)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends