#User function Template for python3
class Solution:
	def getCount(self, n):
		# code here
		if n == 1:
		    return 10

        moves = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8']
        }

        dp = {key: 1 for key in moves.keys()}  # Initial count for sequences of length 1

        for i in range(2, n + 1):
            new_dp = {key: 0 for key in moves.keys()}
            for key in dp.keys():
                for move in moves[key]:
                    new_dp[move] += dp[key]
            dp = new_dp

        return sum(dp.values())


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends