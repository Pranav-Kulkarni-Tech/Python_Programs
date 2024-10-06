def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5),+1):
        if num%i==0:
            return False
    return True
    

def between_prime(start,end):
    num_list=[]
    for n in range(start,end+1):
        if prime(n):
            num_list.append(n)
    return num_list

start=int(input("Enter a starting number"))
end=int(input("ending number"))
new_list=between_prime(start,end)
print(f" between {start}  and  {end} is {new_list} ")