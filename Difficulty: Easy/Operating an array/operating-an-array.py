#{ 
 # Driver Code Starts

# } Driver Code Ends
# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
class Solution:
    
    def searchEle(self,arr, x):
        # Code here
        for i in range(len(arr)):
            if arr[i]== x:
                return 1
            
        return 0
    
    # insert element if you have inserted properly 1 will be printed else 0
    def insertEle(self,arr, y, yi):
        # Code here
        arr.append(0)
        for i in range(len(arr)-1,yi,-1):
            arr[i] = arr[i-1]
        arr[yi] = y
        return 1
    
    # delete element if you have deleted properly 1 will be printed else 0
    def deleteEle(self,arr, z):
        # Code here
        
        if z in arr:
            arr.remove(z)
            return 1
        else:
            return 0
        


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1
        x, y, yi, z = map(int, data[index].split())
        index += 1

        temp = arr[:]
        obj = Solution()

        # searchEle
        if obj.searchEle(arr, x):
            print("true", end=" ")
        else:
            print("false", end=" ")

        # insertEle
        obj.insertEle(arr, y, yi)
        temp.insert(yi, y)
        if arr == temp:
            print("true", end=" ")
        else:
            print("false", end=" ")

        # deleteEle
        obj.deleteEle(arr, z)
        if z in temp:
            temp.remove(z)
        if arr == temp:
            print("true", end=" ")
        else:
            print("false", end=" ")
        print()

# } Driver Code Ends