# print fibonacci series
n=int(input("enter a number"))
f=0
s=1
for i in range(n):
    print(f)
    t=f
    f=s
    s=t+s
   
    
""""
s=f+s print previous steps value of f and s


 step-1               first 0 print
 0           temp=0
        *** first=1  f=s s=1
            second=0+1      f=s and f will print

            print(f) first print previous
step2-     step 1  previous print            
1            t=1  bacause t=f anf f=1
            ***f=1  because f=s s=1
            s=1+1=2 because t=1 and s=1 t+s=1+1=2


            print(f)above            
1    step3  print          t
            t=1
            ***f=2  this print in next step f=s and s=2
             s=1+2=3 s=3 s=f+s 


2       step4   print(f) above step f=2 
        t=2 t=f 
        ***f=3  print next step  f=s s=3 in above
        s=5  f+s=2+3  

3       t=3 t=f 
        ***f=5 f=s 
          s=3+5=8 f=3 s=5 i above 
 
5                   


"""