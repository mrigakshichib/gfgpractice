#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
         # code here 
        mod=10**9+7
        p,q,r=0,1,1
        for i in range(3,n+1):
            a=(p+q)%mod
            r=(2*r+a)%mod
            p=q
            q=a
        return r 

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends