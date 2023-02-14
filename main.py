import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count_reel_one = {
    "A": 1, 
    "B": 3,
    "C": 2,
    "D": 1, 
    "E": 7,
    "F": 5,
    "G": 2, 
    "H": 0
}

symbol_count_reel_two = {
    "A": 1, 
    "B": 2,
    "C": 2,
    "D": 5, 
    "E": 3,
    "F": 5,
    "G": 6, 
    "H": 0
}

symbol_count_reel_three = {
    "A": 1, 
    "B": 1,
    "C": 2,
    "D": 8, 
    "E": 3,
    "F": 4,
    "G": 0, 
    "H": 4
}

def deposit():
    while True:
        amount = input("Enter amount to be deposited: $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to be bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    
    return lines


def get_bet():
    while True:
        amount = input("Enter betting amount for each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")
    
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough funds for that bet, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    


main()