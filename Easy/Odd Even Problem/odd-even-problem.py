
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    
    
        x = 0
        y = 0
    
    
        for char, freq in frequency.items():
            position = ord(char) - ord('a') + 1  # Position in the alphabet (1-based)
            if position % 2 == 0: 
                if freq % 2 == 0:
                    x += 1
            else:
                if freq % 2 == 1:
                    y += 1
    
   
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends