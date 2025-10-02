import math
klas_1 = int(input("Количество учеников в 1 классе"))
klas_2 = int(input("Количество учеников в 2 классе"))
klas_3 = int(input("Количество учеников в 3 классе"))
part=math.ceil((klas_1+klas_2+klas_3)/2)
print("Надо купить ",str(part)," парт")