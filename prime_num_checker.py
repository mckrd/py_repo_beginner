#Hi! I am a beginner to open source and wanted to participate in the Hacktoberfest. I am totally new, so please excuse and let me know if there are any mistakes. Thank you!
#This code is to check if user input is prime or not

num = int(input("Enter number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, " not a prime number")
            break
    else:
        print(num, "is a prime number")
        
else:
    print(num, "is not a prime number")
