#import datetime

#date_now = datetime.datetime(2025, 9, 18)
#date_then =datetime.datetime(2025, 8, 10)

#print(date_diff)


import datetime

print("Skriv in start året")
start_year = input()
start_year = int(start_year)


print("skriv in start månad")
start_month = input()
start_month = int(start_month)

print("skriv in dag")
start_day = input()
start_day =int(start_day)

start_date = datetime.datetime(start_year, start_month, start_day)

print("\nAnge slutdatum:")

end_year = input()

end_year =int(end_year)

end_month =input()
end_month =int(end_month)


end_day =input()
end_day =int(end_day)

end_date =datetime.datetime(end_year, end_month, end_day)

print("skriv in Elmätarensvärde")
start_elmätarensvärde = input()
start_elmätarensvärde =int(start_elmätarensvärde)

print("skriv in Elmätarensvärde")
end_elmätarensvärde = input()
end_elmätarensvärde = int(end_elmätarensvärde)

print("kriv in dagsavgift")

day_fee = input()
day_fee=int(day_fee)

print("skriv in kwH priset")

kwh_price = input()
kwh_price =int(kwh_price)


date_diff = (end_date - start_date).days

el_diff = (end_elmätarensvärde - start_elmätarensvärde)

price = (date_diff * day_fee + el_diff * kwh_price) * 1.25

print(f"Priset blev {price}kr")