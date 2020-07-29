# Find a year to use the Same Canlender

import calendar
import datetime


# get all lucky years in 200 years
def get_lucky_years(this_year):
    lucky_years = []
    this_year_date = [calendar.monthrange(this_year, m) for m in range(1,13)] # date of this year
    for i in range(-100,100):
        lucky_year = this_year + i
        lucky_year_date = [calendar.monthrange(lucky_year, m) for m in range(1,13)] # date of the lucky year
        if lucky_year_date == this_year_date:
            print(f'AHA! Found a lucky year to reuse your calendar: {lucky_year}')
            lucky_years.append(lucky_year)
        i += 1
        continue
    return lucky_years



def main():
    this_year = datetime.datetime.now().year # this year
    lucky_years = get_lucky_years(this_year)
    print(lucky_years)
    return

if __name__ == "__main__":
    main()


