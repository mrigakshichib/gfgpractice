#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    #return True/False
    combined_string = ""
    current = head
    
    while current:
        combined_string += current.data
        current = current.next
    
    # Step 2: Check if the combined string is a palindrome
    return combined_string == combined_string[::-1]

# Helper function to create a linked list from a list of strings
def create_linked_list(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    for item in arr[1:]:
        current.next = Node(item)
        current = current.next
    
    return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n1 = int(input())
        arr1 = input().split()
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        if compute(ll1.head):
            print('true')
        else:
            print('false')

# } Driver Code Ends