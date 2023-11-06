class Sum: 
    def sum_num(a): 
       s=0 
       while a > 0:
           r=a%10  
           s=s+r 
           a=a//10 
       return s 
