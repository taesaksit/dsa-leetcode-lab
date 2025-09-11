from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)

        return result


words = ["abc", "bcd", "aaaa", "cbc"]
x = 'a'

sol = Solution()
result = sol.findWordsContaining(words, x)
print(result)
