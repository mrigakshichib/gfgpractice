#User function Template for python3
#in Bubble sort, what happens is that adjacent elements are comapred till the time we get our sorted array
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        n=len(arr)
        for i in range(n-1):#this loop is for the number of passes that will put the largest number at the end of it
            for j in range(n-i-1):#this loop iterates through the array ,here we put -1 as we shouldnt compare the largest element which has already been put at the right position
                if arr[j+1]<arr[j]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends