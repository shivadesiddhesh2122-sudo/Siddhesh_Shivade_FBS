num= int(input("Enter the three digit number:- "))



num1= num%10
temp= num//10


num2= temp%10
temp= num1//10
num3= temp%10

sum= num1+num2+num3

print(f'Sum of three number is :- {sum}')





