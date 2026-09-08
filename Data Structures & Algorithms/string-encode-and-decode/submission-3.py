class Solution:

    def encode(self, strs: List[str]) -> str:
        stringSend = "" 

        #get str len, add to beginning of string
        # + special character to mark an element
        for string in strs: 
            stringSend += f"{len(string)}#{string}"
        
        return stringSend
            

    def decode(self, s: str) -> List[str]:
        stringReturn = []
        i = 0 #track where next encoded word len. begin

        while i < len(s):
            x = i
            
            while s[x] != "#": 
                x+=1
            
            length = int(s[i:x]) #get string length
            stringReturn.append(s[x+1:length+x+1]) #string slice, add to result arr
            i = x+1+length #update i to get to next string 
        
        return stringReturn

    #first attempt, using special char like # to mark next element
    #fails if the string itself contains specified character. 
    #need more unique delimiter, maybe string length prior