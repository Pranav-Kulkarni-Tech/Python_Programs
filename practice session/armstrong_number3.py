def armstrong(num):
    digits=str(num)
    num_digit=len(digits)
    sum_of= sum(int(digit) ** num_digit for digit in digits)

    if sum_of==num:
        print("armstrong")
    else:
        print("not armstrong")
num=int(input("Enter a number"))
armstrong(num)

