#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        original_A=A
        original_B=B
        while B>0:
            R=int(A%B)
            A=B
            B=R
        GCD=A
        LCM=(original_A*original_B)//GCD
        return LCM,GCD


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends