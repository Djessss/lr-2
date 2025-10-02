import math
x=int(input("Введите х"))
y=int(input("Введите y"))
u=(8+abs(x-y)**2+1)**(1/3)/(x**2+y**2+2)-math.e**abs(x-7)
print("Результат: ",str(u))