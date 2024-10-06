# fibonacci series using generator

def fibo():
    a=0
    b=1
    count=0
    while count<10:
        yield a
        a,b=b,a+b  # a=b  b=a+b
        count=count+1
g=fibo()
for i in g:
    print(i)  

""""
b  value is previous step. b decides what a becomes a=b, b=a+b and next step
  and a is yeild value
step1    a=0  yeild a 

a=b  b=1 a=1  
b=a+b  0+1 b=1  yeild a=0  in above so  a=0 in this step

step2 -yeild a=1
a=b  b=1  a=1  
b=a+b b=1+1=2 b=2  

step3  yeild a a=1
a=b a=2 because b=2
b=a+b  b=2+1 b=3

step4-   yeild a=2
a=b a=3 because previous b=3





"""         
