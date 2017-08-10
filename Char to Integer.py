# Given [1.0, 2.1, -3.3], return 2.1.

class Solution:
    # @param {double[]} A a float array
    # @return {double} a float number
    def maxOfArray(self, A):
        # Write your code here
        max = A[0]
        for e in A:
            if e >= max:
                max = e
            else:
                continue
        return max

solution = Solution()
print(solution.maxOfArray([1.0, 2.1, -3.3]))