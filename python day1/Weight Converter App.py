#WEIGHT CONVERTER APP
weight = float(input("Enter Weight Here: "))
unit = input("for kilograms(K), for Pounds(L):")
if unit.upper() == "K":
    converted = float(weight) * 2.20462
    print("weight in Lbs:" + str(converted) )
elif unit.upper() == "L":
    converted = float(weight) / 2.20462
    print("weight in Kgs:" + str(converted))
else:
    print("please enter K or L")







