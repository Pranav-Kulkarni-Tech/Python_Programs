def palindrome(num):
   rev=0
   x=num
   while num>0:
      rev=(rev*10) + num%10 
      num=num//10
   if rev==x:
      print("palindrome")
   else:
      print("not palindrome") 
    
    

num=int(input("Enter a number"))
palindrome(num)
      
      
