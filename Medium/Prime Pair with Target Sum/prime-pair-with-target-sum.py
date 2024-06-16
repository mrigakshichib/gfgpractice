
from typing import List


class Solution:
    def sieve(self, n: int) -> List[int]:
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        
        prime_list = []
        for p in range(2, n + 1):
            if is_prime[p]:
                prime_list.append(p)
        
        return prime_list
    def getPrimes(self, n : int) -> List[int]:
        # code here
        if n < 4:
            return [-1, -1]
        
        primes = self.sieve(n)
        prime_set = set(primes)
        
        for prime in primes:
            if (n - prime) in prime_set:
                return [prime, n - prime]
        
        return [-1, -1]

        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends