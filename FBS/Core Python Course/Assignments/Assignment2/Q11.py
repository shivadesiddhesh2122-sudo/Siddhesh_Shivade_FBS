amt= int (input("Enter the amount :- "))

n500= amt//500
amt= amt%500

n100= amt//100
amt=amt%100

n50= amt//50
amt=amt%50

n10= amt//10


print(f'500 :- {n500} \n 100 :- {n100} \n 50:- {n50} \n 10:- {n10}')