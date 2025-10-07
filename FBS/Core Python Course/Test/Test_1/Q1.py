l= float(input("Enter the length :-"))
b= float(input("Enter the breadth :-"))
r= float(input("Enter the radius :-"))

area_t= (l*b)+(0.5*3.14*(r**2))

perimeter= l+l+b+(3.14*r)
print(f'Area is {area_t} Peraimeter is {perimeter}')
