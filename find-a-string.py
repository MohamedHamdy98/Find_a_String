#https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

class FindString:
    def __init__(self,stringInput, subStringInput):
        self.stringInput = stringInput
        self.subStringInput = subStringInput

    def findString(self):
        count = 0
        for i in range(len(self.stringInput)):
            if self.stringInput[i:].startswith(self.subStringInput):
                count+=1
        return count

stringInput = input()
subStringInput = input()

obj = FindString(stringInput, subStringInput)

count = obj.findString()
print(count)