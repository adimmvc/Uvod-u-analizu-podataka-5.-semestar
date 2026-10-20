# We have covered the basics during the lab practices with the teaching assistant
# DIY tasks
yearly_consumption = {1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000}
total_for_2026 = 0
for value in yearly_consumption:
    total_for_2026 += value

price_per_kwh = 0.15
total_pay: float | int = total_for_2026 * price_per_kwh
print("Total electricity spent:",total_for_2026)
average = total_pay / len(yearly_consumption)
print("Average electricity spent:",average)
print("Total to pay at the end of the year:",total_pay)

import os
os.system('pause')