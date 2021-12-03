hours = float(input("Hours worked for:"))
hourly_rate = 10.50

if hours <= 40:
    Pay = hourly_rate * hours
    print(f"Your Pay: {Pay}")
elif hours > 40:
    extra_hours = hours - 40
    Pay = (hourly_rate * 40) + (extra_hours * 1.5 * hourly_rate)
    print(f"Your Pay: {Pay}")
#
#
# a= float(input("a: "))
# b= float(input("b: "))
# c = a + b
#
# print(f"The sum of a and b is {c} which i know")

