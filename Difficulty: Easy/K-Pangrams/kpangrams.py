#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        mp = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        
        # Count the frequency of each alphabet letter in the given string
        for x in string:
            if x.isalpha():  # Check if the character is an alphabet letter
                mp[x.lower()] += 1  # Convert to lowercase to handle case insensitivity
        
        zero = 0  # Counter for letters that do not appear in the string
        alph = 0  # Counter for total number of alphabet letters in the string
        
        # Count the number of letters that are missing and total occurrences of letters
        for count in mp.values():
            if count == 0:
                zero += 1
            else:
                alph += count
        
        # If there are not enough distinct letters to form a pangram, return False
        if alph < 26:
            return False
        
        # If the number of missing letters is less than or equal to k, return True
        if zero <= k:
            return True
        
        return False  # Otherwise, return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends