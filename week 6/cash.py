def get_cents():
    while True:
        try:
            cents = float(input("Enter the amount: ")) * 100
            if cents >= 0:
                return round(cents)
        except ValueError:
            print("Invalid input. Please enter a valid amount in dollars.")

def calculate_quarters(cents):
    return cents // 25

def calculate_dimes(cents):
    return cents // 10

def calculate_nickels(cents):
    return cents // 5

def calculate_pennies(cents):
    return cents

def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters
    quarters = calculate_quarters(cents)
    cents -= quarters * 25

    # Calculate the number of dimes
    dimes = calculate_dimes(cents)
    cents -= dimes * 10

    # Calculate the number of nickels
    nickels = calculate_nickels(cents)
    cents -= nickels * 5

    # Calculate the number of pennies
    pennies = calculate_pennies(cents)

    # Sum up the total coins
    total_coins = int(quarters + dimes + nickels + pennies)

    # Print the total number of coins
    print(total_coins)

if __name__ == "__main__":
    main()
