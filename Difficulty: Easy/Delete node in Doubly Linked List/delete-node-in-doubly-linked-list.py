class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Solution:
    def delete_node(self, head, x):
        #code here
        if not head:
            return None
        
        # Store the head node
        current = head
        
        # If head needs to be removed
        if x == 1:
            head = current.next
            if head:
                head.prev = None
            return head
        
        # Traverse the list to find the node to be deleted
        for _ in range(x - 1):
            current = current.next
            if not current:
                return head  # If position is greater than number of nodes
        
        # If node to be deleted is last node
        if current.next:
            current.next.prev = current.prev
        
        if current.prev:
            current.prev.next = current.next
        
        return head

# Utility function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    @staticmethod
    def print_list(node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        head = None
        tail = head

        for i in range(n):
            temp = int(data[index])
            index += 1
            if head is None:
                head = Node(temp)
                tail = head
            else:
                new_node = Node(temp)
                tail.next = new_node
                new_node.prev = tail
                tail = new_node

        x = int(data[index])
        index += 1

        obj = Solution()
        res = obj.delete_node(head, x)

        Node.print_list(res)

# } Driver Code Ends