#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
		# code here
		l=len(arr[0])
		ans=l
		k=-1
		for i in range(len(arr)):
		    for j in range(l):
		        if arr[i][j] == 1:
		            if j-1 < ans:
		                ans=j-1
		                k=i
		            if j-1==-1:
		                return i
		            break
	    return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends