# Write a Python script to display the various Date Time formats.
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import datetime


def show_various_date_formats():
    datetime_obj = datetime.datetime.today()
    print(f'Current date and time: {datetime_obj.strftime("%Y/%m/%d %H:%M:%S")}')
    print(f'Current year: {datetime_obj.strftime("%Y")}')
    print(f'Month of year: {datetime_obj.strftime("%B")}')
    print(f'Week number of the year {datetime_obj.strftime("%W")}')
    print(f'Weekday of the week: {datetime_obj.strftime("%w")}')
    print(f'Day of year: {datetime_obj.strftime("%j")}')
    print(f'Day of the month: {datetime_obj.strftime("%d")}')
    print(f'Day of week: {datetime_obj.strftime("%A")}')


def main():
    show_various_date_formats()


if __name__ == "__main__":
    main()
