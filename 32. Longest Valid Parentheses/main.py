class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        index=0
        maxLen=0
        curLen=0
        for i,t in enumerate(s):
            if(t==')'):
                if((not stack) or stack[-1][1]==1):
                    stack.append((i,1))
                
                else:
                    stack.pop();
                    if not(stack):
                        curLen = i+1;
                    else:
                        curLen = i-stack[-1][0];    
                    maxLen = max(maxLen, curLen);
            else:
                stack.append((i,0))

            
        return maxLen