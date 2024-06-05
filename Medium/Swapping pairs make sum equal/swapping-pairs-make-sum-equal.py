class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum_a = sum(a)
        sum_b = sum(b)
        
        # If sums are already equal, return 1
        if sum_a == sum_b:
            return 1
        
        # Calculate the difference
        diff = sum_a - sum_b
        
        # If the difference is odd, return -1 as it's not possible to equalize the sums
        if diff % 2 != 0:
            return -1
        
        # Calculate the target value
        target = diff // 2
        
        # Convert b to a set for quick lookup
        set_b = set(b)
        
        # Check if there exists an element in a that, when target is subtracted, exists in b
        for value in a:
            if (value - target) in set_b:
                return 1
        
        return -1



#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends