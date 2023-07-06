"""
Almost practically the same as the production version
(see documentation @ 4thworkday.py file).
Debugging-wise, addition of iterating through 200 next months
to verify the fourth business day from several results.
"""

import pandas as pd
import datetime
import calendar
import holidays

today = pd.to_datetime("today").date()
days_in_month = calendar.monthrange(today.year, today.month)[1]
test_dates = pd.date_range(start=today, periods=200, freq="1M")

for td in test_dates:
    start_date = datetime.datetime(year=td.year, month=td.month, day=1)
    end_date = datetime.datetime(year=td.year, month=td.month, day=days_in_month)

    fin_holidays = []
    for date in holidays.Finland(years=td.year).items():
        fin_holidays.append(str(date[0]))

    full_current_business_month = pd.bdate_range(
        start_date, end_date, freq="C", holidays=fin_holidays
    )
    fourth_business_day = full_current_business_month[3].date()
    print(f"{td.month}/{td.year}\n" f"Fourth business day: {fourth_business_day}\n")
