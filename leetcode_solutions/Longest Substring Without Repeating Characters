#https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring( s: str) -> int:
    indices = {}
    string = list(s)
    currentMax= [1]
    if len(string) == 0:
        return 0
    for char in set(string):
        indices[char] = -1
    indices[string[0]] = 0
    for i in range(1,len(string)):
        if indices[string[i]] == -1:
            currentMax.append(currentMax[-1]+1)
            indices[string[i]] = i
        else:
            if string[i] == string[i-1]:                
                currentMax.append(min(currentMax[-1], i-indices[string[i]]))
            else:
                currentMax.append(min(currentMax[-1]+1, i-indices[string[i]]))
            indices[string[i]] = i
    return max(currentMax)

stringToCheck = input().strip()
print(lengthOfLongestSubstring(stringToCheck))
