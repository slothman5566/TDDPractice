class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        
class Solution:
    def maxPoints(self, points):
        length=len(points)
        slope_map={}
        if(length<=2):
            return (length)
        result=0
        for i in range(length):
            samePoint,vertical,slope_max=1,0,0
            slope_map.clear()
            for j in range(i+1,length):
                dx, dy = points[i].x - points[j].x, (points[i].y - points[j].y)
                if dx == 0 and dy == 0:
                    samePoint += 1
                elif dx == 0:
                    vertical += 1
                else:
                    gcd = self.getGcd(dx, dy)
                    dx //= gcd
                    dy //= gcd
                    slope_map[(dx,dy)] = slope_map.get((dx,dy), 0) + 1
                    slope_max = max(slope_max, slope_map[(dx,dy)])
                    
            result = max(result, max(slope_max, vertical) + samePoint)
        
        return result
        
    def getGcd(self, a, b):
        if b == 0: return a
        return self.getGcd(b, a%b)