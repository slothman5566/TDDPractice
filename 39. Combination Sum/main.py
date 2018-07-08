class Solution:

    def solution(self,input,target):
        if not (input):
            return []
        #avoid duplicate and sorted
        return list(self.recursive(sorted(list(set(input))),target,[]))
            
    def recursive(self,input,target,output):
        for i in input:
            if sum(output)+i<target:
                yield from self.recursive(input[input.index(i):],target,list(output+[i]))
            elif (sum(output)+i==target):
                yield list(output+[i])
            else:
                break
