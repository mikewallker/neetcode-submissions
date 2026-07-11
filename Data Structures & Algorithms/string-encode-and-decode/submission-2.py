class Solution:

    def encode(self, strs: List[str]) -> str:
        # count the length of each string
        # append it to str, then append the str[i]
        result = ""
        for word in strs:
            length = len(word)
            result += str(length) + "?" + word
        return result
        # 5?Hello5?World
        # 0?0?

    def decode(self, s: str) -> List[str]:
        result = []
        # loop each item
        # find number and symbol
        # create a list string with length that we already saved
        foundSeparator = False
        wordLength = 0
        wordLengthStr = ""
        tempStr = ""
        for character in s:
            if foundSeparator == True:
                wordLength -= 1
                tempStr += character

                if(wordLength) == 0:
                    foundSeparator = False
                    result.append(tempStr)
                    tempStr = ""

            elif character == "?":
                foundSeparator = True
                wordLength = int(wordLengthStr)
                wordLengthStr = ""

                if wordLength == 0:
                    foundSeparator = False
                    result.append(tempStr)
                    
            else:
                wordLengthStr += character
        return result