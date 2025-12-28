from art import logo

# Print the logo and welcome message
print(logo)
print('Welcome to the secret aucation program.')


# Create an empty dictionary to store bids
bidding_dict = {}

# Flag to control the bidding loop
continue_bidding = True

# Function to find the highest bidder
def  find_highest_bidder():
    winner = ""
    highest_bid = 0
    for  bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ₹{highest_bid}.")

# Continue to ask for bids until there are no more bidders
while continue_bidding:
    # Get bidder's name and bid amount
    name = input("What is your name?: ")
    price = int(input("What is your bid?: ₹"))
    bidding_dict[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    
    if should_continue == 'no':
        continue_bidding = False # Exit the loop
        find_highest_bidder() # Determine and announce the highest bidder
    elif should_continue == 'yes':
        print("\n" * 40) # Clear the console by printing new lines
        
    
    
