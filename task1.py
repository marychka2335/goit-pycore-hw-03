from datetime import datetime
def get_days_from_today(date):
   try: 
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = (input_date - current_date)        
        return delta.days
   except ValueError:
        return (print('Enter the proper data format YYYY-MM-DD'))


print(get_days_from_today('2024-10-09'))


