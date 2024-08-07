
num1=10
num2=20	

if num1>num2:
    pass
    # print("num1 is greater")
else:
    print("num2 is greater")
    
    ##nested if
    if num1>num2:
        print("num1 is greater")
    elif num1==num2:
        print("num1 is equal to num2")
    
    else:
        print("num2 is greater")