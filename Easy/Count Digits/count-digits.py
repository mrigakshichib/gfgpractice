#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
       n_str=str(N)
       count=0
       for i in n_str:
           digint=int(i)
           if digint!=0 and N%digint==0:
               count+=1
       return count       
           
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends