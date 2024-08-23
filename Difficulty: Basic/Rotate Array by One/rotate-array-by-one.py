#User function Template for python3

class Solution:
    def rotate(self, arr):
        '''
        last element first pe aa rha and sabhi elements aage badh rahe hain
        so arr[i] = arr[i+1]
        arr[n-1] = arr[i]
        '''
        n = len(arr)
        last_element = arr[-1]
        for i in range(n-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = last_element
        return arr
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        t -= 1

# } Driver Code Ends