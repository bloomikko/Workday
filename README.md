# Is it workday?
Script for checking is month's XXth day a workday.

The script takes current date, forms a whole business day calendar from the ongoing month and checks what is the fourth business day of the month.
The desired number of day can be changed.
Also handles holidays and the holiday calendar can be changed easily.
Uses pandas and holidays libraries.

# Features
  - Takes current date and compares it whether it is a XXth workday
  - Handles holidays, supports different regional holiday calendars
  - Useful for example for monthly business-critical automation scripts which always happen at certain time

# Example
Assume today is 16th February 2023 - the script checks that current month's fourth business day is 6th February.
As 16th February != 6th February, the script will not continue.
Had today been 6th February, the script would have continued to execute the following commands.
