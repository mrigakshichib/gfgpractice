#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        low, high = 0, len(arr) - 1
        
        # Loop until the search range is valid
        while low <= high:
            mid = (low + high) // 2  # Calculate the middle index
            
            # Check if the middle element is the key
            if arr[mid] == key:
                return mid
            
            # Determine if the left half is sorted
            if arr[low] <= arr[mid]:
                # Check if the key lies within the sorted left half
                if arr[low] <= key < arr[mid]:
                    high = mid - 1  # Search in the left half
                else:
                    low = mid + 1  # Search in the right half
            else:
                # The right half must be sorted
                # Check if the key lies within the sorted right half
                if arr[mid] < key <= arr[high]:
                    low = mid + 1  # Search in the right half
                else:
                    high = mid - 1  # Search in the left half
        
        # If the key is not found, return -1
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends