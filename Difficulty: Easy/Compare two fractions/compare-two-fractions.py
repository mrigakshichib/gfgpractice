#User function Template for python3


class Solution:
    def compareFrac (self, str):
        
        # code here
        fractions = str.split(", ")
    
  
        a, b = map(int, fractions[0].split("/"))
        c, d = map(int, fractions[1].split("/"))
    
   
        lhs = a * d
        rhs = b * c
        if lhs > rhs:
            return fractions[0]
        elif lhs < rhs:
            return fractions[1]
        else:
            return "equal"
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends