#User function Template for python3

class Solution:
    def pattern (self, arr):
        # code here
        def is_palindrome(sub_arr):
            return sub_arr == sub_arr[::-1]
        
        n = len(arr)
        
        # Check for row palindromes
        for i in range(n):
            if is_palindrome(arr[i]):
                return "{} R".format(i)
        
        # Check for column palindromes
        for j in range(n):
            column = [arr[i][j] for i in range(n)]
            if is_palindrome(column):
                return "{} C".format(j)
        
        # If no palindrome is found
        return "-1"




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends