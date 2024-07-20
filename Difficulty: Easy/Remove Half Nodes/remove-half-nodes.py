class Solution:
    def RemoveHalfNodes(self, node):
        #code here
        if node is None:
            return None
        
        # Recursively remove half nodes from the left and right subtrees
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        
        # If the current node is a half node with only a left child, replace it with the left child
        if node.left is not None and node.right is None:
            return node.left
        
        # If the current node is a half node with only a right child, replace it with the right child
        if node.right is not None and node.left is None:
            return node.right
        
        # If the current node is not a half node, return the node as is
        return node

    def inorderTraversal(self, root):
        # Helper function to perform inorder traversal
        result = []
        self._inorderTraversalHelper(root, result)
        return result
    
    def _inorderTraversalHelper(self, node, result):
        if node is not None:
            self._inorderTraversalHelper(node.left, result)
            result.append(node.value)
            self._inorderTraversalHelper(node.right, result)

# Helper function to build a tree from list input (for testing purposes)
def buildTree(values):
    if not values:
        return None
    
    from collections import deque
    iter_values = iter(values)
    root = TreeNode(next(iter_values))
    queue = deque([root])
    
    for value in iter_values:
        current = queue.popleft()
        
        if value is not None:
            current.left = TreeNode(value)
            queue.append(current.left)
        
        if next(iter_values, None) is not None:
            current.right = TreeNode(next(iter_values))
            queue.append(current.right)
    
    return root



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(s):
    if len(s) == 0 or s[0] == 'N':
        return None

    ip = s.split()
    root = Node(int(ip[0]))

    queue = []
    queue.append(root)

    i = 1
    while len(queue) > 0 and i < len(ip):
        currNode = queue.pop(0)
        currVal = ip[i]

        if currVal != 'N':
            currNode.left = Node(int(currVal))
            queue.append(currNode.left)

        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        if currVal != 'N':
            currNode.right = Node(int(currVal))
            queue.append(currNode.right)

        i += 1

    return root


def printInorder(root):
    if root is None:
        return

    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1

    while t > 0:
        s = data[index]
        root = buildTree(s)
        solution = Solution()
        fresh = solution.RemoveHalfNodes(root)
        printInorder(fresh)
        print()
        t -= 1
        index += 1

# } Driver Code Ends