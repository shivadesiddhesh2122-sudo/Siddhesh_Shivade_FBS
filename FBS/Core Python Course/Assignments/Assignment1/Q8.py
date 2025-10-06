days= int(input("Enter days :-"))

years= days//365
# calculate remaining days after calculating years
rdays= days% 365

weeks= rdays//7
# calculate reamining days after calculating weeks
remain_days= rdays%7

print(f'years :- {years} \n Weeks:- {weeks} \n Days :- {remain_days}')