class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        if len(set(sentence)) == 26:
            return True
        else:
            return False


sentence = "thequickbrownfoxjumpsoverthelazydog"
sol = Solution()
result = sol.checkIfPangram(sentence)
