def prime(num):
    if num<=0:
        False  
    else:
        for i in range(2,int(num*0.5)+1):
            if num%i==0:
                return False
    return True


def prime_numbers(start,end):

    prime_list=[]

    
    for i in range(start,end):
        if prime(i):
            prime_list.append(i)
    return prime_list

start=int(input("Enter a starting number"))
end=int(input("Enter end number"))

new_list=prime_numbers(start,end)

print(f"{new_list} ")

        