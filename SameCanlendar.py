# Find a year to use the Same Canlender

import calendar
import datetime
import locale


# get all lucky years in 200 years
def get_lucky_years(this_year):
    lucky_years = []
    this_year_date = [calendar.monthrange(this_year, m) for m in range(1,13)] # date of this year
    for i in range(-100,100):
        lucky_year = this_year + i
        lucky_year_date = [calendar.monthrange(lucky_year, m) for m in range(1,13)] # date of the lucky year
        if lucky_year_date == this_year_date:
            # print(f'AHA! Found a lucky year to reuse your {this_year} calendar: {lucky_year}')
            lucky_years.append(lucky_year)
        i += 1
        continue
    return lucky_years



def main():
    this_year = datetime.datetime.now().year # this year
    lucky_years = get_lucky_years(this_year) # lucky years with the same calendar
    
    years_before = ', '.join([str(year) for year in lucky_years if year < this_year])
    years_after = ', '.join([str(year) for year in lucky_years if year > this_year])

    sys_language,_ = locale.getdefaultlocale() # get system default language

    if sys_language == 'zh_CN':
        print(f'\n恭喜! 你 {this_year} 年的日历可以在 {years_after} 年重复利用哦。')
        print(f'\n稍等... 其实你 {years_before} 年的日历都还可以拿来在今年用呢。')
        
    else:
        print(f'\nCongrats! You can reuse your {this_year} calendar in {years_after}.')
        print(f'\nWait... BTW, You can reuse your {years_before} calendars this year.')

    return

if __name__ == "__main__":
    main()
