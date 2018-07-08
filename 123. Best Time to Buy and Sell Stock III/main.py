import heapq
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not(prices):
            return 0
        print(prices)
        _local =[0,0,0]
        _global=[0,0,0]
        for i in range(len(prices)-1):
            diff=prices[i+1]-prices[i]
            if(diff==0):
                continue
            j=2
            while(j>=1):
                if(diff>0):
                    _local[j] = max(_global[j-1]+diff, _local[j]+diff); 
                else:
                    _local[j] = max(_global[j-1], _local[j]+diff)
                _global[j] = max(_local[j],_global[j])
                j=j-1
            print(_local,_global)
        return _global[2]
    #     record=[]
    #     count=0
    #     for num in (self.calculate_different(prices)):
    #         if(num<0):
    #             record.append(count)
    #             record.append(num)
    #             count=0
    #             continue
    #         count+=num
    #     record.append(count)
    #     temp=[]
    #     dic=heapq.nlargest(2, enumerate(record), key=lambda x: x[1])
    #     minIndex=min(dic, key = lambda t: t[0])[0]+1
    #     maxNumber=0
    #     for i in range(len(record)):
    #         temp=self.Find_Max(record[0:i])+self.Find_Max(record[i:])
    #         print(temp,self.Find_Max(record[0:i]),self.Find_Max(record[i:]))
    #         if(temp>maxNumber):
    #             maxNumber=temp
    #     print(self.calculate_different(prices))
    #     print(record)
    #     # print(record[0:minIndex],record[minIndex:])
    #     # print(self.Find_Max(record[0:minIndex]),self.Find_Max(record[minIndex:]))
    #     print('------------------------')
    #     # return self.Find_Max(record[0:minIndex])+self.Find_Max(record[minIndex:])
    #     return maxNumber
        
    # def calculate_different(self,part):
    #     if(len(part)==1):
    #         return []
    #     if(part and len(part)==2):
    #         return[part[1]-part[0]]
    #     midIndex=int((len(part))/2)
    #     # print(midIndex)
    #     # print(part[midIndex+1],part[midIndex])
    #     return self.calculate_different(part[0:midIndex])+[part[midIndex]-part[midIndex-1]]+self.calculate_different(part[midIndex:])
    
    # def Find_Max(self,numbers):
        
    #     if not(numbers):
    #         return 0
    #     maxNumber=0
    #     count=0
    #     for num in numbers:
            
    #         if( num >maxNumber and maxNumber==0 ):
    #             maxNumber=num
    #         if not(maxNumber==0):
    #             count+=num
            
    #         if(count>maxNumber):
    #             maxNumber=count
    #         if(count>0 and  count<num and num>maxNumber):
    #             maxNumber=num
    #             count=num
                
    #     return maxNumber

        