
hourlyWage = float(input("What's your hourly wage?"))
print("You make {} dollars per hour.".format(hourlyWage))

hoursWorked = float(input("How many hours do you work per day?"))
print("You work {} hours per day.".format(hoursWorked))

daysWorked = int(input("How many days per week do you work?"))
print("You work {} days per week.".format(daysWorked))


grossPay = hourlyWage * hoursWorked * daysWorked
takeHomePay = (grossPay - (grossPay * .15)) # = grossPay(1 - (1 * .15)) =grossPay * .85

print("Your gross pay is {} and your takeHomePay is {}.".format(grossPay,takeHomePay))