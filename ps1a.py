
total_cost = 0
portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = 0
portion_saved = 0
number_of_months = 0

annual_salary = int(input('Enter annual salary: '))
portion_saved = float(input('Enter portion saved: '))
total_cost = int(input('Enter the total cost of your house: '))

monthly_salary = annual_salary / 12

while current_savings <= total_cost * portion_down_payment:
    number_of_months += 1

    return_on_investment = current_savings * r / 12
    current_savings += return_on_investment + (portion_saved * monthly_salary)

print(f'No. of months: {number_of_months}')


