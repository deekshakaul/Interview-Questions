#https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        listing = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = list(s)
        listOfLists = []
        listArray = []
        for i in range(0, len(number)):
            if i == 0:
                listArray.append(number[i])
            elif listing[number[i]] > listing[number[i-1]]:
                listArray.append(number[i])
            else:
                listOfLists.append(listArray)
                listArray = []
                listArray.append(number[i])
        listOfLists.append(listArray)
        sum = 0
        for eachList in listOfLists:
            sum += self.computeNumberUtil(eachList, listing)
        return sum
    
    def computeNumberUtil(self, listArray, listing):
        num = listing[listArray[-1]]
        for index in range(len(listArray)-2, -1, -1):
            num -= listing[listArray[index]]
        return num
