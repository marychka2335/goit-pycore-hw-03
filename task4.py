from datetime import datetime, timedelta


from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_to_birthday = (birthday_this_year - today).days

        if 0 <= days_to_birthday < 7:
            congratulation_date = today + timedelta(days=days_to_birthday)

            if birthday_this_year.weekday() >= 5:
                 ongratulation_date = birthday_this_year + timedelta(days=7 - birthday_this_year.weekday())
            else:
                congratulation_date = birthday_this_year


            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),})
    
    return upcoming_birthdays        


users = [
    {"name": "John Doe", "birthday": "1985.08.23"},
    {"name": "Jane Cole", "birthday": "1990.08.04"},
    {"name": "John Smith", "birthday": "1991.08.05"},
    {"name": "Rick Novak", "birthday": "1995.08.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)