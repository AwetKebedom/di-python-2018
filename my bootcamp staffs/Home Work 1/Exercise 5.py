user_data = int(input("Please write any number\n"))
print(" The divisors of the number are")
for i in range(1,user_data+1):
    if(user_data%i==0):
        print(i)