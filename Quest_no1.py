number = input("Enter a Number = ")
num = float(number)

if num > 0 and num <= 10:
    print("Low Range")
elif num > 10 and num <= 50:
    print("Medium Range")
elif num > 50 and num <= 100:
    print("High Range")
else:
    print("Out of Range")
