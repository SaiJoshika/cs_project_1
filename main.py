from package.Sum import Sum 
from package.Reverse import Reverse 
 
if __name__=="__main__": 
    #Performing Sum of digits of a number
    result=Sum.sum_num(1234)
    print(f"Sum of digits of a number: {result}")
 
    result=Reverse.num(2345)
    print(f"Reverse of a number: {result}")
