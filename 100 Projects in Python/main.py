# hours = float(input("Hours worked for:"))
# hourly_rate = 10.50
#
# if hours <= 40:
#     Pay = hourly_rate * hours
#     print(f"Your Pay: {Pay}")
# elif hours > 40:
#     extra_hours = hours - 40
#     Pay = (hourly_rate * 40) + (extra_hours * 1.5 * hourly_rate)
#     print(f"Your Pay: {Pay}")
#
#
# a= float(input("a: "))
# b= float(input("b: "))
# c = a + b
#
# print(f"The sum of a and b is {c} which i know")


# print(type(5).__name__)

# import twitter
#
# print("Hello")

# largest = None
# smallest = None
lista = []

while True:
    num = input("Enter Number: ")
    if num == "done":
        print("Invalid Input")
        print("Maximum No.", max(lista))
        print("Maximum No.", min(lista))
        break
    else:
        try:
            num = int(num)
            lista.append(num)

        except:
            print("Invalid Input")


