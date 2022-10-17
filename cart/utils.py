from datetime import date

# Take the date from str
def take_date_from_str(form_date):
      list_date = form_date.split('-')
      year = int(list_date[0])
      month = int(list_date[1])
      day = int(list_date[2])
      return date(year, month, day)

# retun a number of days between 2 dates
def num_of_days(date1, date2):
    return (date2-date1).days
