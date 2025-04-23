father_age = int(input("Введіть вік батька: "))
mother_age = int(input("Введіть вік матері: "))

if father_age > mother_age:
    print("Батько старший")
elif mother_age > father_age:
    print("Матір старша")
else:
    print("Батько і матір одного віку")
