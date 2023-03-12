
# 2.17 lab divide input integers
user_num = int(input("Enter the user_num: "))
div_num = int(input("Enter the div_num: "))

for i in range(3):
    result = user_num // div_num
    print(result, end=' ')
    user_num = result

# 2.18 LAB : Driving costs
mileage = float(input("Enter the car's gas mileage (miles per gallon): "))
gas_cost = float(input("Enter the cost of gas: "))

print("{:.2f}".format(gas_cost * (20 / mileage)), end=' ')
print("{:.2f}".format(gas_cost * (75 / mileage)), end=' ')
print("{:.2f}".format(gas_cost * (500 / mileage)))


#2.21 LAB : Using math functions
import math

x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

print("{:.2f}".format(x ** z), end=" ")
print("{:.2f}".format(x ** (y ** z)), end=" ")
print("{:.2f}".format(abs(x - y)), end=" ")
print("{:.2f}".format(math.sqrt(x ** z)))



#2.22 LAB : Expression for calories burned during workout
age = int(input("Enter your age: "))
weight = int(input("Enter your weight in kg: "))
heart_rate = int(input("Enter your heart rate: "))
time = int(input("Enter time in minutes: "))

calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time/8.368

print("Calories : {:.2f} calories".format(calories))



#2.23 LAB : Musical note frequencies
f_initial = int(input("Enter the initial key frequency: "))
r = 2 ** (1/12)

f_current = f_initial
for i in range(5):
    f_current = f_initial * (r ** i)
    print("{1:.2f}".format(i, f_current), end=' ')


#2.25 LAB : Convert to Dollars
quarters = int(input("Enter the count of quarters: "))
dimes = int(input("Enter the count of dimes: "))
nickels = int(input("Enter the count of nickels: "))
pennies = int(input("Enter the count of pennies: "))

total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
total_dollars = total_cents / 100

print("Amount: ${:.2f}".format(total_dollars))

#2.27 LAB : Convert to Seconds
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

time_in_seconds = (hours * 3600) + (minutes * 60) + seconds

print("Seconds: {}".format(time_in_seconds))


#2.28 LAB : Convert from seconds
from datetime import timedelta

time_in_seconds = int(input("Enter the time in seconds: "))
time = timedelta(seconds=time_in_seconds)

print("Hours: {}".format(time.seconds // 3600))
print("Minutes: {}".format((time.seconds % 3600) // 60))
print("Seconds: {}".format((time.seconds % 3600) % 60))



#2.29 LAB : Pizza party
people = int(input("Enter the number of people attending the party: "))
slices_per_person = 2
slices_per_pizza = 12
pizza_cost = 14.95

total_slices = people * slices_per_person
pizzas_needed, remaining_slices = divmod(total_slices, slices_per_pizza)
if remaining_slices != 0:
    pizzas_needed += 1

total_cost = pizzas_needed * pizza_cost

print("Pizzas: {}".format(pizzas_needed))
print("Cost: ${:.2f}".format(total_cost))

#2.30 LAB : Ordering pizza
pizzas = int(input("Enter the number of pizzas to order: "))
pizza_price = 9.99
sales_tax_rate = 0.06

subtotal = pizzas * pizza_price
total = subtotal + (subtotal * sales_tax_rate)

print("Subtotal: ${:.2f}".format(subtotal))
print("Total Due ${:.2f}".format(total))
