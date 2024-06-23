def main():
    print(prompt_for_date("Date: "))

def parse_date(date_string):
    valid_month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if "/" in date_string:
        month, day, year = date_string.split("/")
    else:
        month, day, year = date_string.split(" ")
        month = valid_month_names.index(month) + 1

        if "," in day:
            day = day.strip(",")
        else:
            raise ValueError

    year = int(year)
    month = int(month)
    day = int(day)

    if year < 1:  # https://en.wikipedia.org/wiki/Anno_Domini
        raise ValueError

    if not (0 < month < 13):
        raise ValueError

    if not (0 < day < 32):
        raise ValueError

    return f"{year:>04}-{month:>02}-{day:>02}"

def prompt_for_date(prompt):
    while True:
        try:
            return parse_date(input(prompt))
        except ValueError:
            pass

main()
