class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        if(sum(machines)%len(machines)!=0):
            return -1
        target=sum(machines)/len(machines)
        blance,minMove=0,0
        for machine in machines:
            blance+=machine-target
            minMove=int(max(minMove,max(abs(blance),machine-target)))
        return minMove