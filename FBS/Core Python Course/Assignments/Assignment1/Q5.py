p= int(input("Enter the principle amount:- "))
r= int (input("Enter the Rate:- "))
t= int(input("Enter he time:- "))


a= p*(1+r/100)**t

ci= a-p

print(f'Compound Interest is :- {ci}')
