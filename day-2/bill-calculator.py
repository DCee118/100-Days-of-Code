print('Welcome to my bill calculator')

bill = float(input('What was the total bill? £'))
tip = int(input('How much tip would you like to give? 10%, 12% or 15%? '))
people = int(input('How many people to split the bill? '))

tip_percent = tip/100
total_tip_amount = tip_percent * bill
total_bill = bill + total_tip_amount
total_per_person = total_bill / people
final_total = '{:.2f}'.format(total_per_person)
print(f'Each persom will pay £{final_total}')