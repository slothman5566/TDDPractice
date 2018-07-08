
class Solution:
    def josephus(self,items,k):
        result=[]
        index=0
        while(items):
            index=index+k-1
            if(len(items)<=index):
                index=index%(len(items))
            result.append(items.pop(index))
        return result
        
    
    