# Problem 2
# Write a program that takes today’s date and prints the date of the next week.
# Ex:
# Input: Day: 25 Month: 1 Year: 2025
# Output: Day: 1   Month: 2 Year: 2025

from datetime import datetime, timedelta


day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

current_date = datetime(year, month, day)
next_week_date = current_date + timedelta(days=7)

print(f"Day: {next_week_date.day}   Month: {next_week_date.month}   Year: {next_week_date.year}")
