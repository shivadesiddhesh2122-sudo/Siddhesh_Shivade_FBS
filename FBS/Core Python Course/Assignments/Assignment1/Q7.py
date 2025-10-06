
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate discriminant (b² - 4ac)
D = b*b - 4*a*c


sqrt_D = D ** 0.5

#Apply formula for roots
root1 = (-b + sqrt_D) / (2*a)
root2 = (-b - sqrt_D) / (2*a)


print("First Root =", root1)
print("Second Root =", root2)
