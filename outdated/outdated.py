def main():


def parse_date(date_string):
    if "/" in date_string:
        month, day, year = date_string.split("/")
    else:
        month, day, year = date_string.split(" ")
        month = valid_month_names.index(month) + 1
        day = day.strip(",")
