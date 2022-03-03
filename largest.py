firstnum = int(input("Enter the 1st number"))
secondnum = int(input("Enter the 2nd number"))
thirdnum = int(input("Enter the 3rd number"))
if firstnum > secondnum and firstnum > thirdnum :
    print("The greatest number is", firstnum)
elif secondnum > thirdnum and secondnum > firstnum :
    print("The greatest number is ", secondnum)
else:
    print("The greatest number is ",thirdnum)