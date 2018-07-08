class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i,v in  enumerate(sorted(citations, reverse=True)):
            if(i>=v):
                return i
        return len(citations)