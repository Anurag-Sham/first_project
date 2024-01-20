number=int(input("Enter the number"))

def prime(number):
    value=True
    for num in range(2,number-1):
        if number%num ==0:
            value=False
        

    if value:
        print("Prime")
    else:
        print("Not Prime")



prime(number)