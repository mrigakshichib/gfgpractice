# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        # brute force
        '''if n == 1:
            return 0
        for i in range(len(arr)):
            if i == 0:
                if arr[i]>= arr[i+1]:
                    return i
            elif i == n-1:
                if arr[i]>= arr[i-1]:
                    return i
            else:
                if arr[i]>= arr[i-1] and arr[i]>=arr[i+1]:
                    return i
        return -1'''
        
        
        
        #Optimised approach- using binary search
        #these three are edge cases
        '''if n == 1:
            return 0
        if arr[0]> arr[1]:
            return 0
        if arr[n-1]>arr[n-2]:
            return n-1
        left = 0
        right = n-2 # as we have already checked for n-1 in the edge cases
        while(left<=right):
            mid = (left+right)/2
            if(arr[mid-1]<=arr[mid] and arr[mid]>=arr[mid+1]):
                return mid
            if(arr[mid]>arr[mid-1]):
                left = mid + 1
            else:
                right = mid-1
        return -1'''
        
       
        
        if n == 1:
            return 0

        left = 0
        right = n - 1  # Consider the full range

        while left <= right:
            mid = (left + right) // 2

        # Check if mid is a peak
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
                return mid

        # If the element on the left is greater, move left
            if mid > 0 and arr[mid - 1] > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

            
        



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends