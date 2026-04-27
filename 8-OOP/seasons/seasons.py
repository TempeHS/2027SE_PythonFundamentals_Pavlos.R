from datetime import date
import inflect


def main(date=None):
    if date is None:
        date = input("What is your birthdate? (YYYY-MM-DD)")
    else:
        return split_date(date)
    print(split_date(date))


def split_date(date_str):
    try:
        year, month, day = date_str.split("-")
    except (TypeError, AttributeError, ValueError):
        return "Wrong Input Format"
    else:
        try:
            birth_date = date(int(year), int(month), int(day))
        except ValueError:
            return "Wrong Values Inputted"
        else:
            return date_compare(birth_date)


def date_compare(birth_date):
    current_date = date.today()

    time = current_date - birth_date

    seconds = time.total_seconds()

    if seconds < 0:
        return "Can't be born in the future"
    else:
        return seconds / 60


if __name__ == "__main__":
    main()
