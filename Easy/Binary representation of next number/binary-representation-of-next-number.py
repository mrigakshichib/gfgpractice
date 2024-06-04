#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
		# code here
		binary_list = list(s)
        n = len(binary_list)
        
        carry = 1
        for i in range(n - 1, -1, -1):
            if carry == 0:
              break
            if binary_list[i] == '1':
              binary_list[i] = '0'
              carry = 1
            else:
              binary_list[i] = '1'
              carry = 0
    
   
        if carry == 1:
            binary_list.insert(0, '1')
    
    
        result = ''.join(binary_list)
        return result.lstrip('0')
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)

# } Driver Code Ends