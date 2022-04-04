# You may need to use some functions from the math library for this
# homework, such as math.log(), math.ceil(), and math.floor()
import math


### Problem 1: What Day Were You Born?

# Step 2
def day_of_week(month, day, year):
    adjustedmonth = (month + 9) % 12 + 4
    #print(adjustedmonth)
    adjustedyear = year - adjustedmonth // 14 
    #print(adjustedyear)
    century = adjustedyear // 100
    #print(century)
    centuryyear = adjustedyear % 100
    #print(centuryyear)
    monthcorrection = (adjustedmonth * 26) // 10
    #print(monthcorrection)
    add = day + monthcorrection + centuryyear + centuryyear // 4 + century // 4 + 5 * century
    #print(add)
    final = (add + 6) % 7
    return(final)

day_of_week(1, 13, 2020)
#outputs 1, stands for Monday!

'''
e.g. January 13, 2020
adjusted month = (1+9)%12+4 = 10 + 4 = 14.
adjusted year = 2020-14//14 = 2020-1=2019.
century = 2019//100 = 20.
century year = 2019%100 = 19.
month correction = (26 x 14)//10 = 364//10 = 36.
Add: 13 + 36 + 19 + 19//4 + 20//4 + 5 x 20 =177.
(177+6)%7 = 183%7 = 1, which stands for Monday. Which is right!
'''

# Step 3
def day_of_week_nicer(month, day, year):
    adjustedmonth = (month + 9) % 12 + 4
    #print(adjustedmonth)
    adjustedyear = year - adjustedmonth // 14 
    #print(adjustedyear)
    century = adjustedyear // 100
    #print(century)
    centuryyear = adjustedyear % 100
    #print(centuryyear)
    monthcorrection = (adjustedmonth * 26) // 10
    #print(monthcorrection)
    add = day + monthcorrection + centuryyear + centuryyear // 4 + century // 4 + 5 * century
    #print(add)
    final = (add + 6) % 7
    if final == 1:
        return("Monday")
    elif final == 2:
        return("Tuesday")
    elif final == 3:
        return("Wednesday")
    elif final == 4:
        return("Thursday")
    elif final == 5:
        return("Friday")
    elif final == 6:
        return("Saturday")
    elif final == 0:
        return("Sunday")
    else:
        return("error")
    
day_of_week_nicer(1, 13, 2020)

# Step 4
def days_to_friday(month, day, year):
    if day_of_week(month, day, year) == 6:
        return day_of_week(month, day, year)
    elif day_of_week(month, day, year) == 0:
        return (5 - day_of_week(month, day, year))
    else:
        return((5 - day_of_week(month, day, year)) % 5)    

days_to_friday(1, 13, 2020)


### Problem 2: How long will it take to reach your savings goal?

# Step 1
def number_of_periods(P, r, p, F):
    T = (F + p/r) / (P + p/r)
    N = math.log(T) / math.log(1 + r)
    return(round(N,3))
    
number_of_periods(1000, 0.0025, 100, 20000)


# Step 2
def number_of_periods_nicer(P, r, p, F):
    monthstotal = math.ceil(number_of_periods(P, r, p, F))
    #print(monthstotal)
    years = monthstotal // 12
    #print(years)
    months = monthstotal % 12
    #print(months)
    return(f'{years} years, {months} months')
    #note to self: f-strings do not support objects 

number_of_periods_nicer(1000, 0.0025, 100, 20000)

# Step 3
def total_payment(P, r, p, F):
    return(math.floor(number_of_periods(P, r, p, F)) * p)

total_payment(1000, 0.0025, 100, 20000)
