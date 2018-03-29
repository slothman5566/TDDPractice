class Calculator:
    def calc(self,expr):
        try:
            if(len(expr)==0):
                return 0
            token=expr.split(' ')
            stack=[]
            operation={'+','-','*','/'}
            for i in token:
                if(i in operation) :
                    first,second=stack.pop(),stack.pop()
                    stack.append(str(eval(second+i+first)))
                else:
                    stack.append(i)
            return eval(stack.pop()) if stack else 0  
        except (ZeroDivisionError,TypeError)as e:  
            print(e)
            return str(e)
        
        
    