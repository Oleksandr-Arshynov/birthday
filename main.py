from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    today = date.today()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    birthdays_per_week = {day: [] for day in weekdays}

    if users == []:
        return {}

    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        this_year_birthday = birthday.replace(year=today.year)

        if this_year_birthday < today:
            this_year_birthday = this_year_birthday.replace(year=today.year + 1)

        if today <= this_year_birthday <= today + timedelta(days=7):
            day_name = weekdays[this_year_birthday.weekday()]

            if day_name in ["Saturday", "Sunday"]:
                day_name = "Monday"

            birthdays_per_week[day_name].append(name)

    return {day: names for day, names in birthdays_per_week.items() if names}



if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
