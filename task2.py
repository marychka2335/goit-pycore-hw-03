import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    if not 1 <= min <= max <= 1000 or not min <= quantity <= max:
        return [] 

    lottery_numbers = random.sample(range(min, max + 1), quantity)
    lottery_numbers.sort()
    return lottery_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)