def main():


def parse_date(date_string):
    valid_month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    if "/" in date_string:
        month, day, year = date_string.split("/")
    else:
        month, day, year = date_string.split(" ")
        month = valid_month_names.index(month) + 1
        day = day.strip(",")
