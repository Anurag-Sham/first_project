import math

def fun(height,width,cover):
    area=(height*width)
    result=math.ceil(area/cover)
    return result



height=int(input("Enter the height"))
width=int(input("Enter the width"))
  

cover=int(input("Enter the cover"))
print(fun(height,width,cover))