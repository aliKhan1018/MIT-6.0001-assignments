
portion_down_payment = 0.25
current_savings = 0
r = 0.04

annual_salary = int(input('Enter annual salary: '))
semi_annual_raise = float(input('Enter the semi-annual salary raise: '))
portion_saved = float(input('Enter portion saved: '))
total_cost = int(input('Enter the total cost of your house: '))
monthly_salary = annual_salary / 12

number_of_months = 0
while current_savings <= total_cost * portion_down_payment:
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

    return_on_investment = current_savings * r / 12
    current_savings += return_on_investment + (portion_saved * monthly_salary)

print(f'No. of months: {number_of_months}')



