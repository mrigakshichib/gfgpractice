#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        d1 = n // 100         # Hundreds place
        d2 = (n // 10) % 10   # Tens place
        d3 = n % 10           # Units place

   
        sum_of_cubes = d1**3 + d2**3 + d3**3


        if sum_of_cubes == n:
            return "true"
        else:
            return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends