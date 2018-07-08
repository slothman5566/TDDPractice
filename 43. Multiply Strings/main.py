
class Solution:
    charDict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
      
        return str(self.ConvertStrToInt(num1)*self.ConvertStrToInt(num2))
        
    def ConvertStrToInt(self,num):
        result=0
        index=0
        for v in (num[::-1]):
            result+=self.charDict[v]*(10**index)
            index+=1
        return result