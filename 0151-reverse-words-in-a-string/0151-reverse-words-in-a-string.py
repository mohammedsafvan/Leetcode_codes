class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        arr = s.split()
        for word in reversed(arr):
            output = output + word + " "
        return output.strip()