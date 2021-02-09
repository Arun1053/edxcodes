import math
def polysum(n,s):
    
    def areaOfPolygon(n,s):
        #Pi = 3.1428
        area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return area
    def perimeterOfPolygon(n,s):
        perimeter = n * s
        return perimeter
    sum = areaOfPolygon(n,s) + (perimeterOfPolygon(n,s) ** 2)
    return round(sum,4)
