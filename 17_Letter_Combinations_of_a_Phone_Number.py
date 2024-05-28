from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nokiiia = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        queue = deque()

        if digits:
            queue.append('')

        for digit in digits:
            level_size = len(queue)
            for _ in range(level_size):
                current_combination = queue.popleft()
                for letter in nokiiia[digit]:
                    queue.append(current_combination + letter)

        return list(queue)
            