#User function Template for python3

class Solution:
	def findCoverage(self, matrix):
		# Code here
		n = len(matrix)
        m = len(matrix[0])
        total_coverage = 0
    
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    coverage = 0
                
                # Count ones to the left
                    for k in range(j-1, -1, -1):
                        if matrix[i][k] == 1:
                            coverage += 1
                            break
                        if matrix[i][k] == 0:
                            break
                
                # Count ones to the right
                    for k in range(j+1, m):
                        if matrix[i][k] == 1:
                            coverage += 1
                            break
                        if matrix[i][k] == 0:
                            break
                
                # Count ones above
                    for k in range(i-1, -1, -1):
                        if matrix[k][j] == 1:
                            coverage += 1
                            break
                        if matrix[k][j] == 0:
                            break
                
                # Count ones below
                    for k in range(i+1, n):
                        if matrix[k][j] == 1:
                            coverage += 1
                            break
                        if matrix[k][j] == 0:
                            break
                
                    total_coverage += coverage
                
        return total_coverage



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends