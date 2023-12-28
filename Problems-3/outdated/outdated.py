# # In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

# # Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

# # In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
# # [
# #     "January",
# #     "February",
# #     "March",
# #     "April",
# #     "May",
# #     "June",
# #     "July",
# #     "August",
# #     "September",
# #     "October",
# #     "November",
# #     "December"
# # ]
# # Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.


def main():
    control()


def control():
    while True:
        try:
            date = get_date()
            if format_check(date):
                month, day, year = num_format(date)
            else:
                month, day, year = str_format(date)
            if day == False:
                continue
            print_date(month, day, year)
            break
        except ValueError:
            pass


def format_check(date):
    if "/" in date:
        return True
    else:
        return False


def month_check(month):
    months = month_list()
    i = 0
    while i < 12:
        if months[i] == month:
            return True, i + 1
        i += 1
    return False, i + 1


def get_date():
    return input("Date: ").capitalize()


def num_format(date):
    month, day, year = date.split("/")
    if 0 < int(day) < 32:
        if 0 < int(month) < 13:
            if 0 <= int(year):
                return month, day, year
    return False, False, False


def str_format(date):
    mcheck = False
    month, day, year = date.split()
    if "," in day:
        day = day.strip(",")
        if 0 < int(day) < 32:
            mcheck, month = month_check(month)
            if mcheck == True:
                if 0 <= int(year):
                    return month, day, year
    return False, False, False


def print_date(month, day, year):
    month = int(month)
    day = int(day)
    year = int(year)
    print(f"{year}-{month:02}-{day:02}")


def month_list():
    return [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]


main()

# TO DO List
# 3 dates will be taken, we will check this with the split method
# in numeric dates we will split with /
# we will split with " " in verbal, check for commas and if there is no comma, we will re-enter it, if there is a comma, we will delete the comma and send it to format
# According to the situation, after this application, I will put aside the verbal month printing etc. application function with the months again.
# input format month/day/year -> american system
# he wanted me to assume that a month cannot have more than 31 days, so he gave a list and not dict. I can actually do the advanced example with dict :D
# how many days the months have, we will keep it in another list and if an invalid month is entered, we will get a command again
"""
Recall that a str comes with quite a few methods, per https://docs.python.org/3/library/stdtypes.html#string-methods , including split.
Recall that a list comes with quite a few methods, per https://docs.python.org/3/tutorial/datastructures.html#more-on-lists , among which is index.

Note that you can format an int with leading zeroes with code like
print(f"{n:02}")
wherein, if n is a single digit, it will be prefixed with one 0, per https://docs.python.org/3/library/string.html#format-string-syntax
"""
