# small modulefor the practice functions used in main (2 functions here)
import datetime   # built-in library


def get_today_date():
    # return today date as felt text
    today = datetime.date.today()
    return str(today)


def save_text(filename, text):
    # open file 6 write text inside
    file = open(filename, "a")
    file.write(text + "\n")
    file.close()
