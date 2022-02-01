monthly_salary = input(f"Kāda ir jūsu alga mēnesī? -> ")
monthly_salary = int(monthly_salary)
years_working = input(f"Cik pilnus gadus esiet nostrādājis? -> ")
years_working = int(years_working)
bonus_years = years_working - 2
bonus_total = monthly_salary * 0.15 * bonus_years
if bonus_years <= 0:
    print("Jums vēl nepienākas bonus.")
else:
    print(F"Jusu bonuss par nostrādātiem {years_working} gadiem ir {bonus_total} eur.")

