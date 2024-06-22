class Solution:
    def ExtractNumber(self,sentence): 
        #code here
        words = sentence.split()  # Split the sentence into words
        max_number = -1  # Initialize the max_number to -1, which will be returned if no valid number is found

        for word in words:
            if word.isdigit():
                if '9' not in word:
                    number = int(word)  
                    if number > max_number:
                        max_number = number

        return max_number 


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends