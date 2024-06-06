#User function Template for python3

def max_sum(a,n):
    #code here
    current_value = sum(i * a[i] for i in range(n))
    
    # Calculate the sum of all elements
    sum_of_elements = sum(a)
    
    # Initialize max_value as the current_value
    max_value = current_value
    
    # Iterate through the array to find the maximum sum of i*a[i]
    for i in range(1, n):
        # Compute the next rotation's value based on the previous rotation
        current_value = current_value - sum_of_elements + n * a[i - 1]
        
        # Update the maximum value found
        if current_value > max_value:
            max_value = current_value
    
    return max_value


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends