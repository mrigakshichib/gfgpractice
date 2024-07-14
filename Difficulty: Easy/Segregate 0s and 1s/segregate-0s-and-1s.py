#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
    
        while left < right:
            while arr[left] == 0 and left < right:
                left += 1
         # Decrement right index while we see 1 at right
            while arr[right] == 1 and left < right:
                right -= 1
        
        # If left is smaller than right then there is a 1 at left
        # and a 0 at right. Exchange arr[left] and arr[right]
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
    
        return arr



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        obj.segregate0and1(arr)

        print(*arr)

# } Driver Code Ends