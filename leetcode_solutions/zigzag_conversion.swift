# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if only 1 row or only 1 column, return the string as it is
        if numRows == 1 or numRows >= len(s):
            return s
        # delta indicates the direction if we are going up or down thw matrix
        delta = -1
        row = 0
        result = [[] for i in range(numRows)]
        for char in list(s):
            result[row].append(char)
            if row == 0 or row == numRows - 1:
                # change direction on edges
                delta*=-1 
            row = row+delta
        for i in range(numRows):
            result[i] = "".join(result[i])
        return "".join(result)
