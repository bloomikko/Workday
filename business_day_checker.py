"""
The script takes current date, 
forms a whole business day calendar from the ongoing month
and checks what is the fourth business day of the month.
Checks if the current date (today)
is the fourth business day of the current month.

EXAMPLE
Assume today is 16th February 2023
- the script checks that current month's fourth business day is 6th February.
As 16th February != 6th February, the script will not continue.
Had today been 6th February, the script would have continued
to execute the following commands.
"""
import pandas as pd
import datetime
import calendar
import holidays

# Variable assignments
# - takes today's date and forms a date range of currently ongoing month.
# Calendar has not been formed yet, as holidays must be taken into account.
today = pd.to_datetime("today").date()
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
days_in_month = calendar.monthrange(today.year, today.month)[1]
start_date = datetime.datetime(year=current_year, month=current_month, day=1)
end_date = datetime.datetime(year=current_year, month=current_month, day=days_in_month)

# Holidays library can handle Finnish (and other, if needed)holidays
# - the library is used to form an array of Finnish holidays
fin_holidays = []
for date in holidays.Finland(years=current_year).items():
    fin_holidays.append(str(date[0]))

# Forms the current month's calendar, excluding the weekends and holidays
# - i.e., the calendar formed here only contains business days of the month.
# Takes the fourth business day of the month and assignes it to separate variable.
full_current_business_month = pd.bdate_range(
    start_date, end_date, freq="C", holidays=fin_holidays
)
fourth_business_day = full_current_business_month[3].date()
print(
    f"Ongoing month is {current_month}/{current_year}\n"
    f"Fourth business day of current month is {fourth_business_day}\n"
    f"Today's date is {today}"
)

# Compares today's date to current month's fourth business date
# - if it is, the needed script is executed, otherwise the script exits.
if today == fourth_business_day:
    print("Today IS fourth business day of the month, executing the needed script...")
    # Here comes the command for the script
    print("Job successfully done! 🎉")
else:
    print("Today IS NOT fourth business day of the month, exiting script...")
    exit()
