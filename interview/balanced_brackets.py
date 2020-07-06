'''
Problem: Balanced brackets
You're given a string consisting solely of '(' ')'. 
Determine whether the parentheses are balanced.

Reference: https://binarysearch.io/?ref=dcp
'''

class Solution(object):
    
    def solve(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve("(())"))
