class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber:
            s += chr(ord('A') + (columnNumber-1)%26)
            columnNumber = (columnNumber-1)//26
        return s[::-1]