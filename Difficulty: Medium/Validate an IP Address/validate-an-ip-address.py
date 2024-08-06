#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        l = 0
        u = 255
        c = 0
        r = str.split(".")
        for i in r:
            if l<=int(i) and int(i)<=u:
                c+=1
            if c==4:
                return True
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends