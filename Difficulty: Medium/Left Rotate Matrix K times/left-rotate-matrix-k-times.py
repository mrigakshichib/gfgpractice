class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        rows = len(mat)
        cols = len(mat[0]) if rows > 0 else 0
        k = k % cols
        for i in range(rows):
            mat[i] = mat[i][k:] + mat[i][:k]
        
        return mat



#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends