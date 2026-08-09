# Coke Machine

def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]
    
    # Loop until the user has inserted at least 50 cents
    while amount_due > 0:
        # Inform the user of the amount due
        print(f"Amount Due: {amount_due}")
        
        # Prompt the user to insert a coin
        coin_str = input("Insert Coin: ")
        
        # Try to convert the input to an integer
        try:
            coin = int(coin_str)
        except ValueError:
            # If the input is not a valid integer, ignore it
            continue
            
        # Ignore any coin that is not an accepted denomination
        if coin in accepted_coins:
            amount_due -= coin
            
    # Calculate and output how many cents in change the user is owed
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
