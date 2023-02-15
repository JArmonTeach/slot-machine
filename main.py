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

symbol_value = {
    "A": 3, 
    "B": 6,
    "C": 6,
    "D": 14, 
    "E": 13,
    "F": 14,
    "G": 8, 
    "H": 4
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols_one, symbols_two, symbols_three):
    reel_one_symbols = []
    for symbol, symbol_count_reel_one in symbols_one.items():
        for _ in range(symbol_count_reel_one):
            reel_one_symbols.append(symbol)

    reel_two_symbols = []
    for symbol, symbol_count_reel_two in symbols_two.items():
        for _ in range(symbol_count_reel_two):
            reel_two_symbols.append(symbol)

    reel_three_symbols = []
    for symbol, symbol_count_reel_three in symbols_three.items():
        for _ in range(symbol_count_reel_three):
            reel_three_symbols.append(symbol)

    columns = []
    
    column_one = []
    current_symbols_from_one = reel_one_symbols[:]
    for _ in range(rows):
        value_one = random.choice(current_symbols_from_one)
        current_symbols_from_one.remove(value_one)
        column_one.append(value_one)
    columns.append(column_one)

    column_two = []
    current_symbols_from_two = reel_two_symbols[:]
    for _ in range(rows):
        value_two = random.choice(current_symbols_from_two)
        current_symbols_from_two.remove(value_two)
        column_two.append(value_two)
    columns.append(column_two)
    
    column_three = []
    current_symbols_from_three = reel_three_symbols[:]
    for _ in range(rows):
        value_three = random.choice(current_symbols_from_three)
        current_symbols_from_three.remove(value_three)
        column_three.append(value_three)
    columns.append(column_three)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")
        
        print()


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


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough funds for that bet, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count_reel_one, symbol_count_reel_two, symbol_count_reel_three) 
    
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on line(s):", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q" or balance == 0:
                break
        balance += spin(balance)

    print(f"You left with ${balance}.")


main()